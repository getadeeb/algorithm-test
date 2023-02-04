from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for index, ch in enumerate(pattern):
        table[ord(pattern[index])] = index
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)
        self.index = 0

    def decide_slide_width(self, c: str) -> int:
        unicode_ch = -1
        if ord(c) in self.table:
            unicode_ch = self.table[ord(c)]
        slide_width = max(1, self.index - unicode_ch)
        return slide_width

    def __matchPattern(self, shift: int):
        self.index = len(self.pattern) - 1
        while self.index >= 0 and self.pattern[self.index] == self.text[shift + self.index]:
            self.index -= 1

    def search(self) -> int:
        pattern_length = len(self.pattern)
        text_length = len(self.text)
        shift = 0
        while shift <= text_length - pattern_length:
            self.__matchPattern(shift)
            if self.index < 0:
                return shift
            else:
                shift += self.decide_slide_width(self.text[shift + self.index])
        return -1

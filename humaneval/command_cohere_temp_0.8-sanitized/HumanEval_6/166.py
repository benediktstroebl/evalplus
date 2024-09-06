from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(1 + c // 8 for c in char_count(s, i)) for i, _ in enumerate(s.split())]
def char_count(s: str, c: int) -> int:
    return s.count(c) - s.count(c, c)
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(map(len, filter(str.isalpha, group.replace(' ', '')))) + 1 for group in s.split()]
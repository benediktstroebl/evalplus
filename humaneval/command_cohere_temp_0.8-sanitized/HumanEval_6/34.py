from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(parens_level(group)) for group in s.split(' ')]
def parens_level(s: str) -> int:
    if not s:
        return 0
    return 1 + max(parens_level(part) for part in s.split(')'))
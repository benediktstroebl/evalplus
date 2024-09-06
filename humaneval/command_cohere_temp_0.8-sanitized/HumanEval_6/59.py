from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting_level(group)) for group in s.split()]
def nesting_level(s: str) -> int:
    if not s:
        return 0
    return 1 + max(nesting_level(part) for part in s.split(')'))
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting_level(group)) for group in s.split(' ') if group]
def nesting_level(s: str) -> int:
    if not s:
        return 0
    nesting_level = 0
    for char in s:
        if char == '(':
            nesting_level += 1
        elif char == ')':
            nesting_level -= 1
    return nesting_level
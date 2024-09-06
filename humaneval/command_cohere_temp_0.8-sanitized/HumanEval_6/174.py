from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting_level(group)) for group in s.split(' ') if group]
def nesting_level(s: str) -> int:
    level, i = 0, 0
    while i < len(s):
        if s[i] == '(':
            level += 1
        elif s[i] == ')':
            level -= 1
        i += 1
    return level
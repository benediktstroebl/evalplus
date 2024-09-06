from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        nesting_level = 0
        for char in partition:
            if char == '(':
                nesting_level += 1
            elif char == ')':
                nesting_level -= 1
            level = max(level, nesting_level)
        result.append(level)
    return result
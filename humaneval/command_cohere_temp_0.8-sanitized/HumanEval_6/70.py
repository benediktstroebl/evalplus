from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        nesting_level = 0
        for char in bracket_level:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
                if level == 0 and nesting_level > 0:
                    nesting_level -= 1
        result.append(nesting_level)
    return result
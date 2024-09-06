from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        level = 0
        nesting_level = 0
        for char in bracket_str:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
                if level == 0:
                    nesting_level += 1
                if level < 0:
                    return []
        result.append(nesting_level)
    return result
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        nesting_level = 0
        for char in segment:
            if char == '(':
                nesting_level += 1
            elif char == ')':
                nesting_level -= 1
            else:
                pass
            level = max(level, nesting_level)
        result.append(level)
    return result
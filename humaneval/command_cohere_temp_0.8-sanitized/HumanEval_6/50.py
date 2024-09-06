from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        nesting_level = 0
        for char in segment:
            if char == '(':
                depth += 1
                nesting_level += 1
            elif char == ')':
                depth -= 1
                nesting_level -= 1
        result.append(nesting_level)
    return result
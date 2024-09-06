from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        current_depth = 0
        for char in chunk:
            if char == '(':
                current_depth += 1
            elif char == ')':
                current_depth -= 1
            result.append(current_depth)
    return result
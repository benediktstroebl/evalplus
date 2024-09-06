from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result, current_level = [], 0
    for token in s.split():
        if token == '(':
            current_level += 1
        elif token == ')':
            current_level -= 1
        result.append(current_level)
    return result
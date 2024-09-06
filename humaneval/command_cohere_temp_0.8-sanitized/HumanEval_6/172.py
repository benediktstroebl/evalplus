from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result, level = [], 0
    for token in s.split():
        if token == '(':
            level += 1
        elif token == ')':
            level -= 1
        result.append(level)
    return result
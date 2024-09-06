from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair_str in s.split():
        level = 0
        for char in bracket_pair_str:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
            result.append(level)
    return result
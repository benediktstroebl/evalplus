from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        count = 0
        opening_brackets = 1
        for char in bracket_group:
            if char == '(':
                opening_brackets += 1
            elif char == ')':
                opening_brackets -= 1
            count = max(count, opening_brackets)
        result.append(count)
    return result
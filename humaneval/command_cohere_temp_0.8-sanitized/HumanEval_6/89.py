from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        stack = []
        opening, closing = 0, 0
        for char in bracket_group:
            if char == '(':
                opening += 1
            elif char == ')':
                closing += 1
            stack.append(opening)
            stack.append(closing)
        result.append(max(stack))
    return result
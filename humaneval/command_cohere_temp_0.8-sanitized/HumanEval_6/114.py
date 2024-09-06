from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, forClosing = 0, 0
    curlyBraces = 0
    for char in s:
        if char == '(':
            forOpening += 1
        elif char == ')':
            forClosing += 1
        elif char == '{':
            curlyBraces += 1
        elif char == '}':
            curlyBraces -= 1
        result.append(forOpening + forClosing + curlyBraces)
    return result
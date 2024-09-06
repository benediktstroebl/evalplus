from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i, nested = 0, 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            nested = nested + 1 if nested < 0 else 0
        elif char == ')':
            forOpening -= 1
            nested = nested - 1 if nested > 0 else 0
        if forOpening == 0:
            result.append(nested)
            i += 1
            nested = 0
    return result
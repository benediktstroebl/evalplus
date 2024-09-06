from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nesting = 0
        nonlocal result
        for char in chunk:
            if char == '(':
                nesting += 1
            elif char == ')':
                nesting -= 1
            count = max(count, nesting)
        result.append(count)
    return result
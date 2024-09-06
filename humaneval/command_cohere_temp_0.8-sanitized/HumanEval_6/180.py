from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nesting = 0
        for char in chunk:
            if char == '(':
                nesting += 1
            else:
                nesting -= 1
            count = max(count, nesting)
        result.append(count)
    return result
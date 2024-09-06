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
                if nesting > count:
                    count = nesting
            else:
                nesting -= 1
        result.append(count)
    return result
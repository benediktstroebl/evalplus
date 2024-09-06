from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
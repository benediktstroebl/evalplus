from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        for c in chunk:
            if c == '(':
                nest += 1
            else:
                nest -= 1
        result.append(nest)
    return result
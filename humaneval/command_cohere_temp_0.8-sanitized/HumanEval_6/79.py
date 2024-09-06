from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nest = 0
        imbalance = 0
        for c in chunk:
            if c == '(':
                nest += 1
                imbalance += 1
            elif c == ')':
                nest -= 1
                imbalance -= 1
            if imbalance > 0:
                result.append(nest)
                imbalance = 0
    return result
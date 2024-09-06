from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        imbalance = 0
        for char in segment:
            if char == '(':
                nest += 1
                imbalance += 1
            else:
                nest -= 1
                imbalance -= 1
            if imbalance > 0:
                result.append(nest)
                imbalance = 0
    return result
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tier in s.split():
        nesting = 0
        imbalance = 0
        for char in tier:
            if char == '(':
                imbalance += 1
            else:
                imbalance -= 1
            nesting = max(nesting, imbalance)
        result.append(nesting)
    return result
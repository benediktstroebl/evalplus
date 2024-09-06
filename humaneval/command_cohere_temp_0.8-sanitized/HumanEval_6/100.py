from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i, maxLevel = 0, 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            i += 1
            if forOpening > maxLevel:
                maxLevel = forOpening
        else:
            forOpening -= 1
        result.append(maxLevel)
    return result
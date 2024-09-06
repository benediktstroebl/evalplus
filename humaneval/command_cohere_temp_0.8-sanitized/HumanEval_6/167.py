from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nested = 0
        for char in chunk:
            if char == '(':
                nested += 1
            else:
                nested -= 1
                if nested == 0:
                    count = max(count, nested)
        result.append(count)
    return result
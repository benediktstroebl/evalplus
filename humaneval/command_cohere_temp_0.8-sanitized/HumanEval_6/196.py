from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result, count = [], 0
    for token in s.split():
        if token == '(':
            count += 1
        else:
            count -= 1
        result.append(count)
    return result
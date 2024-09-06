from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        counter = 0
        for c in chunk:
            if c == '(':
                counter += 1
            else:
                counter -= 1
        result.append(counter)
    return result
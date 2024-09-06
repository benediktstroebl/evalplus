from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nest in s.split():
        counter = 0
        opener = 0
        for c in nest:
            if c == '(':
                opener += 1
            else:
                counter += opener
                opener = 0
        counter += opener
        result.append(counter)
    return result
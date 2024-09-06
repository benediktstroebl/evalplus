from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for interval, level in enumerate(s.split(), 1):
        open, close = 0, 0
        for char in level:
            if char == '(':
                open += 1
            else:
                close += 1
        result.append(max(open, close))
    return result
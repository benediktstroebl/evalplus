from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        counter = 0
        opening = chunk.count('(')
        closing = chunk.count(')')
        counter += opening - closing
        result.append(counter)
    return result
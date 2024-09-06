from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        counter = 0
        while opening != closing:
            counter += 1
            opening = opening.count('(')
            closing = closing.count(')')
        result.append(counter)
    return result
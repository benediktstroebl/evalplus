from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nest = 0
        found = 0
        while opening != closing:
            if opening == '(':
                nest += 1
                opening = closing
                found += 1
            elif closing == ')':
                nest -= 1
                closing = opening
                found += 1
            if nest > depth:
                depth = nest
        result.append(found)
    return result
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nested = 0
        while opening != closing:
            if opening == '(':
                depth += 1
            elif closing == ')':
                depth -= 1
                nested += depth
            opening = closing
        result.append(nested)
    return result
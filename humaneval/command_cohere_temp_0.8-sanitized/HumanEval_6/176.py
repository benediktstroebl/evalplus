from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        curr = opening
        while curr != closing:
            if curr == '(':
                depth += 1
            else:
                depth -= 1
            curr = next(closing)
        result.append(depth)
    return result
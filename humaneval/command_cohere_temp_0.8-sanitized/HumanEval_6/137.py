from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        nesting = 0
        i = 0
        for i, char in enumerate(segment):
            if char == '(':
                nesting += 1
            elif char == ')':
                nesting -= 1
            if nesting < 0:
                break
            depth = max(nesting, depth)
        result.append(depth)
    return result
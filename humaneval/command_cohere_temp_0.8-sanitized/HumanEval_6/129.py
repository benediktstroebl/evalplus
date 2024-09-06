from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        stack = []
        depth = 0
        for char in token:
            if char == '(':
                stack.append(depth)
                depth += 1
            else:
                depth = stack.pop()
        result.append(depth)
    return result
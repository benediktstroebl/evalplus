from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        stack = []
        for c in chunk:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
        result.append(len(stack))
    return result
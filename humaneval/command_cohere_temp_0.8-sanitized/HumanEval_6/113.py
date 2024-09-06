from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        stack = []
        for char in chunk:
            if char == '(':
                stack.append(stack.append)
            else:
                stack.pop()
        result.append(len(stack))
    return result
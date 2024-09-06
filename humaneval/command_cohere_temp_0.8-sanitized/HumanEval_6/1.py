from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result, stack = [], []
    for char in s:
        if char == '(':
            stack.append(len(stack))
        elif char == ')':
            result.append(len(stack))
            stack.pop()
    return result
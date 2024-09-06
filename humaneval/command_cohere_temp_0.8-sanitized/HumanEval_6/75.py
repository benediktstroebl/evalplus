from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result: List[int] = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            open_parens = len(stack)
            if open_parens:
                stack.pop()
            result.append(open_parens)
    return result
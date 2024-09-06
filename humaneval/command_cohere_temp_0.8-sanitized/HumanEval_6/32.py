from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, group in enumerate(s.split()):
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))
    return result
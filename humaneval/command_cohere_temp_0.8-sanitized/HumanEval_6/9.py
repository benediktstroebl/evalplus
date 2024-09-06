from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        stack = []
        for char in segment:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))
    return result
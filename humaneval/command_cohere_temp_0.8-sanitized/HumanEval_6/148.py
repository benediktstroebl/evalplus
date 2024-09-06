from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        stack = [0]
        for char in segment:
            if char == '(':
                stack.append(open_brackets[-1] + 1 if open_brackets else 1)
                open_brackets.append(stack[-1])
            elif char == ')':
                open_brackets.pop()
                stack.pop()
        result.append(stack[-1])
    return result
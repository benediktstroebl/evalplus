from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        for c in s:
            if c == opener:
                stack.append(stack[-1] + 1)
            elif c == closer:
                stack.pop()
        result.append(stack[-1])
    return result
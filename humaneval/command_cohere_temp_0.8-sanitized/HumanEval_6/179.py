from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for ch in s:
            if ch == opener:
                stack.append(level)
                level += 1
            elif ch == closer:
                level = stack.pop()
        result.append(level)
    return result
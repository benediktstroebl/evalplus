from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
            elif c == Closer:
                level = stack.pop()
            else:
                if opener in c:
                    level += 1
                elif Closer in c:
                    level -= 1
        result.append(level)
    return result
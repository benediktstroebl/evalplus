from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
            elif c == closer:
                level = stack.pop()
                if stack:
                    result.append(level)
            else:
                level += 1
        if stack:
            result.append(stack.pop())
    return result
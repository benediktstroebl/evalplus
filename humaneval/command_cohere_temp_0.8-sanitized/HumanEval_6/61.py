from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(opener)
            elif c == closer:
                if stack:
                    stack.pop()
                    level += 1
                else:
                    result.append(level)
            elif c != ' ':
                stack.append(c)
        result.append(level)
    return result
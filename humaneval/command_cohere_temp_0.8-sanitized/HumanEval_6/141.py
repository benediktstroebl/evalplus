from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
            elif c == closer:
                level = stack.pop() if stack else 0
            else:
                level += 1
        result.append(level)
    return result
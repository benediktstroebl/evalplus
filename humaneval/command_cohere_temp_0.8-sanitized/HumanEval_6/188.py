from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = [0]
        level = 0
        for ch in s:
            if ch == opener:
                stack.append(level)
            elif ch == closer:
                level = stack.pop()
                if stack:
                    result.append(max(level, stack[-1]))
            else:
                level += 1
        if stack:
            result.append(max(level, stack[-1]))
    return result
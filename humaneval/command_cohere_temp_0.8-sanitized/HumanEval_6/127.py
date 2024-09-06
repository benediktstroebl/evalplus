from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for ch in s:
            if ch == opener:
                stack.append(opener)
            if ch == closer:
                if stack:
                    level += 1
                    stack.pop()
                else:
                    result.append(level)
        if stack: 
            result.append(level + 1) 
    return result
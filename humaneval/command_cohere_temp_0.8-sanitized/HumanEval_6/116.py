from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('([{', ')]}'):  
        stack, deepest = [0], 0
        for c in s:
            if c == ' ':
                if stack:
                    result.append(deepest)
                deepest, *stack = stack[:]
            elif c == opener:
                stack.append(deepest)
            elif c == Closer:
                stack.pop()
                deepest = max(deepest, *stack)
        result.append(deepest)
    return result
```python
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
``` 

This code defines a function `parse_nested_parens` that takes a string `s` as input and returns a list of deepest levels of nesting of parentheses in each group separated by spaces. It uses a list `stack` to keep track of openers and checks if each closer is the match for the last opener to determine the deepest level of nesting for each group. The `zip('([{', ')]}')` tuple is used to generate the iterators of openers and closers for checking matches. It also handles cases with extra closing parentheses to correctly determine the nesting level.
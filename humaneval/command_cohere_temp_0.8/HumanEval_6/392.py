```python
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
```

The `parse_nested_parens` function takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces. It iterates through the string, keeping track of the current nesting level in a stack. When an opening parenthesis is encountered, it pushes the current nesting level onto the stack. When a closing parenthesis is encountered, it pops the last nesting level from the stack and adds it to the result list. If the stack is not empty, it also adds the current nesting level to the result. Finally, the function returns the resulting list of deepest levels of nesting for each group.
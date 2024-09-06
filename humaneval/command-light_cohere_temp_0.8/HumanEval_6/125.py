```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    curr_level = 0
    out = []
    for char in s:
        if char == "(":
            if curr_level == 0:
                stack.append(1)
                curr_level += 1
        elif curr_level > 0 and char == ")":
            stack.pop()
            curr_level -= 1
        else:
            if curr_level == 0:
                out.append(char)
                curr_level += 1
            elif curr_level > 0:
                out.append(curr_level)
    return out
```

This function parses a string of nested parentheses. It starts at the basic indentation and follows the rules:
- When an open parenthesis `( )` is encountered, it is pushed onto the stack.
- When a closing parenthesis `)` is encountered, the corresponding element is popped from the stack, and the level is decremented.
- If an intermediate character, it represents the current level of nesting, and is added to the output.
- The function returns a list of the deepest level of nesting of parentheses.
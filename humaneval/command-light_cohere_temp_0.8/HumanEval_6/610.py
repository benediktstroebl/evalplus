```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = False
    output = []
    for c in s:
        if opening and c == "(":
            stack.append(1)
        opening = False
        elif closing and c == ")":
            stack.pop()
            closing = False
        elif c.is_closing_open() and not closing:
            stack.append(0)
        opening = True
        elif c == " ":
            stack.append(1 if opening else 0)
        else:
            stack.append(0)
        output.return = stack
        return output
```
The `parse_nested_parens` function accepts a string of nested parentheses as input and returns a list of the deepest level of nesting of parentheses in the string. It uses a stack to keep track of the current opening and closing parentheses, and it traverses the string character by character, updating the stack accordingly.
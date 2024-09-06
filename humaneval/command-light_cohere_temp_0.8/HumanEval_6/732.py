```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open, close = '(( )', '))'
    output = []

    for char in s:
        if char == open:
            stack.append(0)
        elif char == close:
            top_level = stack.pop()
            level = top_level[1]
            if not level:
                continue
            output.append(level)
            stack.append(0)
        return output
```

This Python function `parse_nested_parens` takes a string of characters as input and returns a list of integer levels of the deepest nesting parentheses found in the string. It uses a stack data structure to keep track of open and closed parentheses. The function iterates through each character in the string, and if the character is the open parenthesis, it pushes a 0 onto the stack. If the character is the close parenthesis, it pops the top level from the stack, gets the level of the popped element, appends this level to the output, and pushes a 0 onto the stack to keep track of the next open parenthesis.
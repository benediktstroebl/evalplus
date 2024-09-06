```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for char in parent_string:
        if char == '(':  # Start of new group
          stack.append(1)
        output.
        stack.append(0)  # End of previous group
          if char == ')':
            stack.pop()  # Output for closing parenthesis
          output.append(stack.pop())
    last one-level group.  # If empty stack for no closing paren. 
return output
```
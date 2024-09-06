```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == ')':  # Match closing parenthesis
          stack.append(len)
          if len(stack) > 0:  # Pop the top level and continue
            stack.append(0)
        else:  # Open parenthesis, push onto stack and continue
              stack.append(1)
    else:  # Continue with any other character
          output.append(stack.pop())
   
    wrap it stack)
    return output
```
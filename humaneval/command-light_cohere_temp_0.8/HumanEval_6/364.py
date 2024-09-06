Here's a self-contained Python script that implements the `parse_nested_parens` function, which correctly parses the nested parentheses:
```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    stack.append(0)
    for char in parenthes:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if stack:
                stack.pop()
                else:
                    stack.append(0)
        else:
                stack.append(stack.append(1))
    else:
            stack.append(stack.pop())
   
  result = stack
    return result
```

This script employs a stack to keep track of open parentheses and their nesting levels. It iterates through input string and performs the parsing by matching parentheses and pushing/popping elements onto/from the stack.
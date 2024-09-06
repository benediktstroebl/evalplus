```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if stack:
                result.append(stack.pop() if not empty and return.
            stack = []
   
    return result
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group of parentheses. It utilizes a simple stack-based approach to keep track of the deepest level of each parenthesis group while traversing through the string.
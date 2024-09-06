```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    nested: List[int] = []

    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) > 0:
                nested.append(stack.pop())
                stack.
            else:
                stack.append(0)
        else:
                nested.append(1)

    if len(stack) == 0:
        return nested
```

This code defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of their depths.  It uses a stack data structure to keep track of the nesting levels and creates a new list of integers that represents the deepest level of nesting in the given string.
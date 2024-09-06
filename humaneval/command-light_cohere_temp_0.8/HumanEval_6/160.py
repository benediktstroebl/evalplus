Here's a self-contained Python script that defines a function `parse_nested_parens` to solve the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                level = stack.pop()
                maximum_level = len(stack)
                result.append(maximum_level)
            stack.clear()
        for i in range(len(stack)):
                stack.append(stack[i] + 1)
            else:
                break
        else:
            stack.append(char)
    return result
```

This script provides a function to parse nested parentheses in a string and returns the deepest level of nesting as a list of integers. It uses a `List` for tracking stack levels and correctly pops items off the stack to determine the maximum nesting level.
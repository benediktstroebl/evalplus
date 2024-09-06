Here's the Python code that implements the `parse_nested_parens` function from the response:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    start = 0
    outputs = []
    for char in parentheses_string:
        if char == '(':
            stack.append(start)
        start = 0
    if char == ')':
            if stack:
                outputs.append(stack.pop()
        stack, if char != '('
    return outputs
```
This script defines a function `parse_nested_parens` that takes a string of parentheses as input and returns a list of corresponding deepest nesting levels of parentheses in the string. This function utilizes a nested lists to keep track of the deepest levels of nesting and uses a stack data structure to keep track of opening parentheses.
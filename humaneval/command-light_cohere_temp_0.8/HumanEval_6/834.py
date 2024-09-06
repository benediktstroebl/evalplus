```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    nesting = 0
    output = []
    for char in parenthes_string:
        if char == '(':
            nesting += 1
        elif char == ')':
            nesting -= 1
        else:
            stack.push(nesting)
        if nesting == 0:
            output.append(stack.pop()
    10 times) will a list to handle the stack and return the correct order of nesting.

# Example usage
result = parse_nested_parens('(()()) ((())) () ((()))()')
result
```
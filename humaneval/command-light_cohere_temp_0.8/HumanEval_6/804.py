```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == "(":
            stack.append(0)
        elif char == ")":
            if stack:
                result.append(stack.pop()
               
    shallowest deepest = True
            stack.pop()
    result.append(0)
        stack.append(1)
    elif char == "(" and stack:
        stack.append(1)
        elif char == ")":
            stack.append(2)
    elif char == "(" and stack:
        stack.append(3)
    stack.pop() result.append(0)
    shallowest = True
    stack.pop() result.append(1)
    if char == ")":
        stack.append(4)
    stack.append(5)
    stack.pop() result.append(0)
    shallow = True
    return result

# Test the function with various inputs
# Test with multiple nested parentheses separated by spaces
# Test with different combinations of parentheses and nested groups
```
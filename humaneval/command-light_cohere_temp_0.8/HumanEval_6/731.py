```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    Input is a string with multiple groups of parentheses separated by spaces. 
    The function returns the levels of nesting for each group of parentheses
    """
    stack: List[int] = []
    for char in parenthes_string:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                stack.append(0)
        else:
                stack.append(stack.append(0)
        else:
                stack.append(1)
    return stack
```
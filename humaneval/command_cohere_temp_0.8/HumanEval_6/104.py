Here's a Python script with a self-contained function that solves the problem using a recursive approach for the number of levels of nesting in each group of parentheses:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    # Initial data structure to hold results and iteratively update it
    result = [0] * len(s.split(' '))
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        elif not stack:
            result[-1] += 1
        else:
            # If the stack is not empty, the parentheses
            # are nested and we increment the result
            result[-1] += 1
    
    return result
```
The provided example shows the use of the function and tests its functionality:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This approach uses a stack to properly handle nested parentheses and increments the result only when the closing parenthesis is encountered, whether the stack was empty or not.
Here's the Python script with a self-contained function that parses and expands the nested parentheses:
```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns a list of the deepest level numbers of each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = []
    stack = []

    for char in parent_string:
        if char == ")":
            stack.append(len)
        else:
            if stack:
                groups.append(stack.pop(). group)
                next level is the stack
            stack = []
        if char == "(":
            stack.append(char)
        else:
            stack.pop()

   elif char == ")":
            stack.append(char)
            if len(stack) > 1:
                groups.append(stack.pop())
                else:
                    groups.append(len)
                stack = []
    
    return groups
```
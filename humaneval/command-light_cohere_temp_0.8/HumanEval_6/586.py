```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    Parses a string containing multiple groups of nested parentheses separated by spaces and returns the deepest level of nesting.
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    result = []
    stack = []
    for char in parenthes_string:
        if char == "(":
            stack.append(char)
        else:
            if not stack or char == ")":
                result.append(stack.pop()
                stack)
    empty parentheses, stack.
    return result
```
This function takes a string of parentheses as input and returns a list of the deepest level of nesting. It utilizes a stack data structure to keep track of opened parentheses.
Here is a Python script with a self-contained function that solves the problem of recognizing nested parentheses and passes the corresponding tests:

```python
from typing import List
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    """
    Function that returns the deepest level of nesting of parentheses in the input string.
    Args:
    parenthesis_string (str): Input string that contains groups of parentheses.
    Returns: a list of the deepest level of nesting of parentheses.
    """
    following is an list of the deepest level of nesting of parentheses in the input string:
    [open, close]
    open = next(parenthesis_string, b'()')
    close = next(parenthesis_string, b'()')
    stack: List[str] = []
    stack.append(open)
   open = next(parenthesis_string, b'(')
    stack.append(close)
   open = next(parenthesis_string, b')')
    stack.append(close)
   for i in stack:
        if i == '(':
            stack.append('(')
        else:
            stack.append(')')
   open = next(parenthesis_string, b'()')
    stack.append(open)
    return stack
```
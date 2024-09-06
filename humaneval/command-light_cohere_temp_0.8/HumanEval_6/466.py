```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses and returns a list of their deepest nesting levels.

    Parameters:
    s (str) is the input string containing multiple groups of parentheses.

    Returns:
    A list of deepest nesting levels of parentheses.
    """
    example:
    >>> parse_nested_parens('(()()) ((())) () ((()))')
    [2, 3, 1, 3]
    """
    result = []
    stack = []
    in_string = False
    for c in s:
        if c == '(':
            if not:
                stack.append(0)
                in_string = True
            stack[-1] += 1
        elif c == ')':
            if not:
                stack.pop()
                in_string = False
            stack[-1] -= 1
        else:
            in_string = False if c == ')' else True if c == ' ' else False
        result.append(stack)
    return result
```
This code provides a self-contained function to parse and count the deepest nesting levels of parentheses in a given string.
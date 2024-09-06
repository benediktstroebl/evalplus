```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with nested parentheses as input and returns a list of its deepest nested levels.

    :For example, given the input '(())() ((()))()', the function would return [2, 3].

    Parentheses are parsed from left to right.
    """
    strings which are not necessarily delimited, so this function 
    accounts for that.
 return a list of their deepest nested levels of parentheses.
"""
def parse_parentheses(input_string: str) -> List[int]:
    stack = []
    in_string = False
    result = []

    for char in input_string:
        if char == '(':
            if in_string:
                stack.append(1)
            in_string = True
        else:
            in_string = True
        if char == ')':
            if not in_string:
                stack.pop()
            in_string = False
        elif in_string:
            stack.append(1)
            in_string = True
        else:
            in_string = False

    if not in_string:
        stack.pop()

    return stack

  return result
```
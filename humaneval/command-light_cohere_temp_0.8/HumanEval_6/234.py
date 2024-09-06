```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns a list of their deepest nesting levels.
    The nested parentheses are represented as '()' and the input string could contain any number of ')' pairs, and can be nested to any depth.
    """
    format of the strings like any of the following:
    '(()()) ((())) () ((())()())'
    [2, 3, 1, 3]
    or
    '( Bar )()()()'

    If the string is not well formed, the function will return an empty list.
    """
    format of
    (parent_string)

    Test cases:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    >>> parse_nested_parens(') )')
    []
    >>> parse_nested_parens('(())'
    []
    """
    stack = []
    for char in parent_string:
        if char == "(":
            stack.append(0)
        elif char == ")":
            if len(stack) == 0:
                return []
            top_level = stack.pop()
            else:
                stack.append(0)
        return stack
    return stack

This function uses a stack to keep track of the nesting levels of the parentheses. It iterates over the different variations of the input string and returns a list of the deepest nesting levels.
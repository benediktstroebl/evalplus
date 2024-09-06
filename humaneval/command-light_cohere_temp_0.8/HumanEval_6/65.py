Here's a self-contained Python script that defines a function parse_nested_parens to solve the provided markdown code block problem:
```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns a list of the deepest nesting levels.
    """
   
    list of integers, with each integer representing the level of nesting of a parenthesis.
    """
    list of integers is returned.
    """
    complex string to parse is "((()))""

    Examples:
    >>> parse_nested_parens('(()()) ((()))() ((()))()())')
    [2, 3, 1, 3]
    """

    # Use a simple depth-first search to find the deepest level of each parenthesis
    # Mark the current position as the deepest level
    levels = []
    current_level = 0
    in_string = False
    for char in s:
        if char == "(" and not in_string:
            in_string = True
        elif char == ")" and in_string:
            in_string = False
            levels.append(current_level)
        elif char == ")":
            current_level += 1

    return levels
```
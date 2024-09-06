```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse a string containing nested parentheses.
    It takes a input to this function is a string containing multiple groups of parentheses separated by spaces.

    The function returns a deepest level of nesting of parentheses in the input string.
    """
    levels = []  # Initialize an empty list to store the deepest level of nesting

    for group in parent_string:  # Iterate through each group of parentheses
        if group == '(':  # If the group is '(', add one to the levels list
            levels.append(1)
        elif group == ')':  # If the group is ')', remove the first occurrence of ')' from the levels list
            levels.pop(0)
        else:  # If the group is not '(' or ')', add 1 to the levels list
            levels.append(1)

    # Return the deepest level of nesting as the list of levels
    return levels  # Return the list of levels containing the deepest level of nesting
```
This function parses a string containing multiple groups of parentheses separated by spaces and returns the deepest level of nesting. The function works by iterating through each group of parentheses in the string, and for each group, it checks if it is '(', adding one to the levels list, if it is not ')', or if it is ')', removing the first occurrence of ')', and then returning the list of levels containing the deepest level of nesting.

This is a self-contained Python function that uses the typing module to define function parameters and returns the List[int] result type.
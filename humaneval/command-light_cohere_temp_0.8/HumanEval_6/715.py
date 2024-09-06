```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse a string with nested parentheses. It returns a maximum nesting level of each group of parentheses in the string.
    Args:
    parent_string (str): The string to parse and identify the nesting level of each group of parentheses.
    Returns: list of int.
    """ Each group of level of nesting.
    """ Example level of nesting represents the count of open parentheses in the group.
def parse_nested_parens(parent_string: str):
    # Split the string into a list of substrings
    substrings = parent_string.split()
    _ the split()
    # Initialize an empty list to store the nesting levels of each group of parentheses
    nested_levels = []
    # Iterate over the substrings and get the nesting level of each group of parentheses
    for i, substring in enumerate(substrings, start=1):
        # Remove any whitespace at the beginning of the substring
        while substring.startswith():
            substring = substring[1:]
        # Initialize the level as 0 if it's the first group of parentheses
        if i == 1:
            nested_levels.append(0)
        # Otherwise the nesting level of the current group of parentheses
        else:
            nested_levels.append(nested_levels[i-1] + 1)
    # Return the list of nesting levels
    return nested_levels
```
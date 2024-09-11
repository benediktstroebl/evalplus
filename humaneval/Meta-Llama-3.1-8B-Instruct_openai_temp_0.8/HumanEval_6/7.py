```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Use regular expression to find all groups of nested parentheses
    groups = re.findall(r'\((?:\([^()]*\)|[^()]*)+\)', paren_string)

    # Initialize an empty list to store the results
    result = []

    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current nesting level
        level = 0
        # Initialize a flag to indicate if we are inside parentheses
        inside = False

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the level
            if char == '(':
                level += 1
                inside = True
            # If the character is a closing parenthesis, decrement the level
            elif char == ')':
                level -= 1
                # If the level becomes negative, it means there is a mismatch in the parentheses
                if level < 0:
                    level = 0
                inside = False
            # If we are inside parentheses and the character is not a parenthesis, ignore it

        # Append the maximum nesting level to the result list
        result.append(level)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses regular expression to find all groups of nested parentheses in the input string. Then it iterates over each group and keeps track of the current nesting level by incrementing it for every opening parenthesis and decrementing it for every closing parenthesis. The maximum nesting level for each group is then appended to the result list.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string with groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    result = []

    # Iterate over each group
    for group in groups:
        # Initialize counters for the current and maximum nesting levels
        curr_nesting = 0
        max_nesting = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, increment the current nesting level
            if char == '(':
                curr_nesting += 1
                max_nesting = max(max_nesting, curr_nesting)
            # If the character is a close parenthesis, decrement the current nesting level
            elif char == ')':
                curr_nesting -= 1

        # Append the maximum nesting level for the group to the result list
        result.append(max_nesting)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses separated by spaces as input. It splits the string into groups, then for each group, it iterates over each character, keeping track of the current and maximum nesting levels. Finally, it returns a list of the maximum nesting levels for each group. The script includes a test case at the end to demonstrate the function's usage.
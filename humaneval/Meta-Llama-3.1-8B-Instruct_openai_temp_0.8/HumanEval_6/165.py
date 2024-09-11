```python
from typing import List
import re


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Use a regular expression to count the number of pairs of parentheses
        count = 0
        max_depth = 0
        depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
                count += 1
        # Append the result to the list
        results.append(max_depth)

    return results

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by splitting the input string into groups, then for each group, it counts the number of pairs of parentheses and the maximum depth of the parentheses. It does this by iterating over the characters in the group, incrementing a depth counter when it encounters an open parenthesis and decrementing when it encounters a close parenthesis. The maximum depth seen during this process is the answer for that group. The script then returns a list of the maximum depths for all groups.
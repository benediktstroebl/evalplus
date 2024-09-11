```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of the deepest level of nesting 
    for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses 
                             separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # split the input string into groups
    max_depths = []  # initialize a list to store the maximum depths

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        current_depth = 0  # initialize the current depth for the current group

        for char in group:
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increment the current depth
                max_depth = max(max_depth, current_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrement the current depth

        max_depths.append(max_depth)  # append the maximum depth for the current group

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces. It splits the input string into groups and then iterates over each group to find the maximum depth of nesting. The maximum depths for all groups are returned as a list.

The script uses a simple iterative approach to find the maximum depth of nesting for each group. It keeps track of the current depth and the maximum depth seen so far for each group. When it encounters an opening parenthesis, it increments the current depth and updates the maximum depth if necessary. When it encounters a closing parenthesis, it decrements the current depth.
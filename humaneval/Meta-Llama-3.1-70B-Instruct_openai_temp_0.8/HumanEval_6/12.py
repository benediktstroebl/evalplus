```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting of parentheses for each group in the input string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.
    """
    groups = paren_string.split()  # split the input string into groups
    max_depths = []  # initialize a list to store the maximum depths

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        current_depth = 0  # initialize the current depth

        for char in group:  # iterate over each character in the group
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increment the current depth
                max_depth = max(max_depth, current_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrement the current depth

        max_depths.append(max_depth)  # append the maximum depth to the list

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the maximum depth of nesting for each group. The function uses a simple iterative approach to keep track of the current depth and updates the maximum depth whenever it encounters an opening parenthesis. The results are returned as a list of integers.
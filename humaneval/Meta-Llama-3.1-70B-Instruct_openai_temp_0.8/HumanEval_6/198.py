```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # split the input string into groups
    max_depths = []  # initialize a list to store the maximum depths

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        curr_depth = 0  # initialize the current depth

        for char in group:  # iterate over each character in the group
            if char == '(':  # if the character is an opening parenthesis
                curr_depth += 1  # increment the current depth
                max_depth = max(max_depth, curr_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                curr_depth -= 1  # decrement the current depth

        max_depths.append(max_depth)  # append the maximum depth to the list

    return max_depths  # return the list of maximum depths


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces, and returns a list of integers representing the deepest level of nesting for each group. It uses a simple iterative approach to calculate the maximum depth for each group.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses in the input string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group of parentheses.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()  # split the input string into groups of parentheses
    max_depths = []  # initialize an empty list to store the maximum depths

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        current_depth = 0  # initialize the current depth

        for char in group:
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increment the current depth
                max_depth = max(max_depth, current_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrement the current depth

        max_depths.append(max_depth)  # append the maximum depth to the list

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```
This script works by iterating over each character in each group of parentheses and keeping track of the current depth. Whenever it encounters an opening parenthesis, it increments the current depth, and whenever it encounters a closing parenthesis, it decrements the current depth. The maximum depth for each group is updated whenever the current depth exceeds the maximum depth. Finally, the maximum depths for all groups are returned as a list.
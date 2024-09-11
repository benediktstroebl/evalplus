```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum level of nesting for each group of parentheses in the input string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum level of nesting for each group of parentheses.
    """
    groups = paren_string.split()  # Split the input string into groups of parentheses
    max_levels = []  # Initialize an empty list to store the maximum levels of nesting

    for group in groups:
        max_level = 0  # Initialize the maximum level of nesting for the current group
        current_level = 0  # Initialize the current level of nesting

        for char in group:  # Iterate over each character in the group
            if char == '(':  # If the character is an opening parenthesis
                current_level += 1  # Increase the current level of nesting
                max_level = max(max_level, current_level)  # Update the maximum level of nesting
            elif char == ')':  # If the character is a closing parenthesis
                current_level -= 1  # Decrease the current level of nesting

        max_levels.append(max_level)  # Append the maximum level of nesting for the current group to the result list

    return max_levels


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the maximum level of nesting for each group of parentheses. The function splits the input string into groups, iterates over each group, and uses a simple counter to keep track of the current level of nesting. The maximum level of nesting for each group is updated accordingly and appended to the result list.
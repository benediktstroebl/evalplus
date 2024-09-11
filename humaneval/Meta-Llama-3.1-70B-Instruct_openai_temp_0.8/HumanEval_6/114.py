```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum nesting level of parentheses in each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum nesting level of each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    max_levels = []  # Initialize a list to store the maximum nesting levels

    for group in groups:
        max_level = 0  # Initialize the maximum nesting level for the current group
        current_level = 0  # Initialize the current nesting level

        for char in group:
            if char == '(':  # If the character is an opening parenthesis
                current_level += 1  # Increase the current nesting level
                max_level = max(max_level, current_level)  # Update the maximum nesting level
            elif char == ')':  # If the character is a closing parenthesis
                current_level -= 1  # Decrease the current nesting level

        max_levels.append(max_level)  # Append the maximum nesting level to the result list

    return max_levels


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This Python script defines a function `parse_nested_parens` that takes a string of parentheses groups as input, calculates the maximum nesting level of each group, and returns a list of these levels. It iterates over each character in each group, updating the current and maximum nesting levels as it encounters opening and closing parentheses.
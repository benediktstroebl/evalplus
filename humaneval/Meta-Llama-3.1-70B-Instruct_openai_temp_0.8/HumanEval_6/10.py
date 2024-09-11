```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    max_levels = []  # Initialize a list to store the maximum levels of nesting

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
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses in a string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group of parentheses.
    """
    groups = paren_string.split()  # Split the string into groups of parentheses
    max_depths = []  # Initialize a list to store the maximum depth of each group

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth for the current group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis, increase the current depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis, decrease the current depth
                current_depth -= 1

        max_depths.append(max_depth)  # Append the maximum depth of the current group to the list

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
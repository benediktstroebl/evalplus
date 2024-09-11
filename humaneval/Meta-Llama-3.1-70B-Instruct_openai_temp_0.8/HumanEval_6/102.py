```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nested parentheses in each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.

    """
    groups = paren_string.split()  # Split the input string into groups
    max_depths = []  # Initialize a list to store the maximum depths

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth

        for char in group:
            if char == '(':  # If the character is an opening parenthesis, increase the current depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis, decrease the current depth
                current_depth -= 1

        max_depths.append(max_depth)  # Append the maximum depth to the list

    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
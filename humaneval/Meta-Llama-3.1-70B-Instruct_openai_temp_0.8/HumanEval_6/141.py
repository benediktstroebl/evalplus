```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses 
    in each group of parentheses separated by spaces.

    Args:
    paren_string (str): A string containing multiple groups of nested 
                        parentheses separated by spaces.

    Returns:
    List[int]: A list of integers where each integer represents the 
               deepest level of nesting of parentheses in each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    result = []  # Initialize a list to store the results

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth for the current group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis
                current_depth += 1  # Increase the current depth
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis
                current_depth -= 1  # Decrease the current depth

        result.append(max_depth)  # Append the maximum depth for the current group to the result list

    return result

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by iterating over each group of parentheses in the input string, then iterating over each character in the group. It keeps track of the current depth of nesting and updates the maximum depth whenever it encounters an opening parenthesis. When it encounters a closing parenthesis, it decreases the current depth. Finally, it appends the maximum depth for each group to the result list.
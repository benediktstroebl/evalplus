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
    groups = paren_string.split()  # Split the string into groups
    result = []  # Initialize a list to store the results

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth for the current group

        # Iterate over each character in the group
        for char in group:
            if char == '(':  # If the character is an opening parenthesis
                current_depth += 1  # Increase the current depth
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis
                current_depth -= 1  # Decrease the current depth

        result.append(max_depth)  # Append the maximum depth for the current group to the result list

    return result  # Return the result list

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
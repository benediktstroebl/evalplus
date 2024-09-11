```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses 
    for each group of parentheses in a given string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses 
                        separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting 
               for each group of parentheses.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Initialize an empty list to store the results
    max_depths = []

    # Iterate over each group of parentheses
    for group in paren_groups:
        # Initialize a counter to keep track of the current depth
        depth = 0
        # Initialize a variable to store the maximum depth
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the depth
            if char == '(':
                depth += 1
                # Update the maximum depth if necessary
                max_depth = max(max_depth, depth)
            # If the character is a closing parenthesis, decrement the depth
            elif char == ')':
                depth -= 1

        # Append the maximum depth for this group to the results list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
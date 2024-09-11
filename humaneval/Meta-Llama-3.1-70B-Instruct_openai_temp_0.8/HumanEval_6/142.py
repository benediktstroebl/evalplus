```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses 
    in each group of parentheses separated by spaces in the input string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses 
                         separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting 
               of parentheses in each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter to keep track of the current level of nesting
        level = 0
        
        # Initialize a variable to store the maximum level of nesting
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the level
            if char == '(':
                level += 1
                # Update the maximum level if necessary
                max_level = max(max_level, level)
            # If the character is a closing parenthesis, decrement the level
            elif char == ')':
                level -= 1

        # Append the maximum level of nesting for the current group to the results
        results.append(max_level)

    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
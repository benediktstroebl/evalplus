```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """

    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in paren_groups:
        # Initialize the current level and maximum level to 0
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                current_level += 1
                # Update the maximum level if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                current_level -= 1

        # Append the maximum level for the current group to the results list
        results.append(max_level)

    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
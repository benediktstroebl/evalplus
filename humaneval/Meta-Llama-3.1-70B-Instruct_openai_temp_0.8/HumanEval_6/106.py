```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current level of nesting and the maximum level of nesting
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level of nesting
            if char == '(':
                current_level += 1
                # Update the maximum level of nesting if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level of nesting
            elif char == ')':
                current_level -= 1

        # Append the maximum level of nesting for the current group to the results list
        results.append(max_level)

    # Return the list of results
    return results


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
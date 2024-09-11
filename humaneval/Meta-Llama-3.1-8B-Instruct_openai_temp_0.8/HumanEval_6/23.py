```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    # Split the input string into individual groups
    groups = paren_string.split()

    def calculate_depth(group: str) -> int:
        """
        Calculate the deepest level of nesting for a single group of parentheses.

        Args:
            group (str): A string representing a group of nested parentheses.

        Returns:
            int: The deepest level of nesting for the group.
        """
        # Initialize the current depth and maximum depth to 0
        current_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if necessary
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                current_depth -= 1

        # Return the maximum depth
        return max_depth

    # Calculate the deepest level of nesting for each group and return as a list
    return [calculate_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses separated by spaces as input. It splits the input string into individual groups and then defines a helper function `calculate_depth` to calculate the deepest level of nesting for each group. The `calculate_depth` function iterates over each character in the group, updating the current depth and maximum depth as necessary. Finally, the script tests the `parse_nested_parens` function with an example input and prints the output.
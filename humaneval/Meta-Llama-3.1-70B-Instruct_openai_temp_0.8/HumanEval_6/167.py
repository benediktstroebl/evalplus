```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting for each group of parentheses in a given string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def calculate_nesting(group: str) -> int:
        """
        Helper function to calculate the deepest level of nesting for a single group of parentheses.

        Args:
            group (str): A string containing a single group of parentheses.

        Returns:
            int: The deepest level of nesting for the given group of parentheses.
        """
        max_nesting = 0
        current_nesting = 0
        for char in group:
            if char == '(':
                current_nesting += 1
                max_nesting = max(max_nesting, current_nesting)
            elif char == ')':
                current_nesting -= 1
        return max_nesting

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Calculate the deepest level of nesting for each group
    nesting_levels = [calculate_nesting(group) for group in groups]

    return nesting_levels

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of parentheses as input, splits it into individual groups, and calculates the deepest level of nesting for each group using a helper function `calculate_nesting`. The result is a list of integers representing the deepest level of nesting for each group of parentheses.
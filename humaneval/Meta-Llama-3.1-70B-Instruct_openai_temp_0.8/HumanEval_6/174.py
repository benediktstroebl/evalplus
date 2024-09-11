```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it returns the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """

    def calculate_nesting(paren_group: str) -> int:
        """
        Helper function to calculate the deepest level of nesting for a single group of parentheses.

        Args:
            paren_group (str): A string containing a single group of nested parentheses.

        Returns:
            int: The deepest level of nesting for the given group.
        """
        max_nesting = 0
        current_nesting = 0

        for char in paren_group:
            if char == '(':
                current_nesting += 1
                max_nesting = max(max_nesting, current_nesting)
            elif char == ')':
                current_nesting -= 1

        return max_nesting

    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Calculate the deepest level of nesting for each group
    nesting_levels = [calculate_nesting(group) for group in paren_groups]

    return nesting_levels


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
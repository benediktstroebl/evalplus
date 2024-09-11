```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting(group: str) -> int:
        """
        Calculate the deepest level of nesting for a single group of parentheses.

        Args:
            group (str): A string containing a group of nested parentheses.

        Returns:
            int: The deepest level of nesting for the group.
        """
        max_level = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
            # If current_level is negative, it means there's a mismatch in the parentheses
            if current_level < 0:
                raise ValueError("Invalid parentheses in the input string")
        # If current_level is not zero, it means there are unmatched open parentheses
        if current_level!= 0:
            raise ValueError("Invalid parentheses in the input string")
        return max_level

    # Split the input string into groups and calculate the deepest level of nesting for each group
    groups = paren_string.split()
    nesting_levels = [max_nesting(group) for group in groups]
    return nesting_levels


# Example usage
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses as input. For each group, it calculates the deepest level of nesting by iterating through the string and keeping track of the current level of nesting. The `max_nesting` function is used to calculate the deepest level of nesting for a single group. The script then splits the input string into groups and uses a list comprehension to calculate the deepest level of nesting for each group.
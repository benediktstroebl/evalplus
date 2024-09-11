```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    It returns a list of integers, where each integer represents the maximum depth of nesting in a corresponding group.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum depth of nesting in each group.
    """

    def max_depth(group: str) -> int:
        """
        Helper function to calculate the maximum depth of nesting in a single group.

        Args:
            group (str): A string of nested parentheses.

        Returns:
            int: The maximum depth of nesting in the group.
        """
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth of nesting in each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input and returns a list of integers representing the maximum depth of nesting in each group. The function uses a helper function `max_depth` to calculate the maximum depth of nesting in a single group.
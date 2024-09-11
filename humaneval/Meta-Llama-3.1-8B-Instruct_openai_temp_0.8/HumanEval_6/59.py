```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    It returns a list of integers representing the maximum level of nesting for each group.

    :param paren_string: A string of groups of nested parentheses separated by spaces.
    :return: A list of integers representing the maximum level of nesting for each group.
    """

    def max_nesting_level(group: str) -> int:
        """
        This is a helper function to calculate the maximum level of nesting for a single group.

        :param group: A string of nested parentheses.
        :return: The maximum level of nesting for the group.
        """
        max_level = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    # Split the input string into groups
    groups = paren_string.split()
    # Calculate the maximum level of nesting for each group
    nesting_levels = [max_nesting_level(group) for group in groups]
    return nesting_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses separated by spaces and returns a list of integers representing the maximum level of nesting for each group. It uses a helper function `max_nesting_level` to calculate the maximum level of nesting for a single group. The function splits the input string into groups, calculates the maximum level of nesting for each group, and returns the list of nesting levels.
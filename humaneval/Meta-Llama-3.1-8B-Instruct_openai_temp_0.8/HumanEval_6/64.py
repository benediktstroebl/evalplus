```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of nested parentheses and return the maximum depth of each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """
        Calculate the maximum depth of a single group of nested parentheses.

        Args:
        s (str): A string containing a group of nested parentheses.

        Returns:
        int: The maximum depth of the group.
        """
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into individual groups and calculate the maximum depth of each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `max_depth` that calculates the maximum depth of a single group of nested parentheses. The main function `parse_nested_parens` splits the input string into individual groups, calculates the maximum depth of each group using `max_depth`, and returns the results as a list.
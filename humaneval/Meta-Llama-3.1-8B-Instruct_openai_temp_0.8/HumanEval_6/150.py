```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of grouped nested parentheses and return the maximum depth of each group.

    Args:
    paren_string (str): A string of multiple groups for nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """Helper function to calculate the maximum depth of a single group of parentheses."""
        max_depth = 0
        depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Calculate the maximum depth of each group
    max_depths = [max_depth(group) for group in groups]

    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script defines a function `parse_nested_parens` that takes a string of grouped nested parentheses as input. It splits the string into individual groups, calculates the maximum depth of each group using a helper function `max_depth`, and returns a list of maximum depths. The `max_depth` function iterates over the characters in a group, incrementing and decrementing a depth counter as it encounters open and close parentheses, respectively, keeping track of the maximum depth encountered. The main function then applies this helper function to each group in the input string and returns the results.
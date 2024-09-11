```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses and returns a list of integers.
    Each integer represents the maximum depth of nesting of parentheses in its corresponding group.

    Args:
        paren_string (str): A string of groups of nested parentheses. Each group is separated by a space.

    Returns:
        List[int]: A list of integers representing the maximum depth of nesting of parentheses in each group.
    """

    def max_depth(group: str) -> int:
        """Helper function to calculate maximum depth of a group of nested parentheses."""
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups of nested parentheses
    groups = paren_string.split()

    # Calculate the maximum depth of nesting for each group
    max_depths = [max_depth(group) for group in groups]

    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses and returns a list of integers, where each integer represents the maximum depth of nesting of parentheses in its corresponding group. The function uses a helper function `max_depth` to calculate the maximum depth of a group of nested parentheses. The `max_depth` function iterates over the characters in the group, incrementing a depth counter when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. The maximum depth encountered during this process is returned as the result. The main function splits the input string into groups, calculates the maximum depth of nesting for each group using the `max_depth` function, and returns the list of maximum depths.
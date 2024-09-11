```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(string: str) -> int:
        """Helper function to find the maximum depth of nested parentheses."""
        depth = 0
        max_depth = 0
        for char in string:
            if char == '(':
                # Increase depth when opening parentheses is encountered
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                # Decrease depth when closing parentheses is encountered
                depth -= 1
        return max_depth

    # Split the input string by spaces and return the maximum depth of each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string containing multiple groups of nested parentheses as input. It uses a helper function `max_depth` to calculate the maximum depth of nested parentheses for each group. The `max_depth` function iterates through the characters in a string, increasing the depth when an opening parenthesis is encountered and decreasing the depth when a closing parenthesis is encountered. The maximum depth encountered during this process is returned as the result. The `parse_nested_parens` function splits the input string by spaces, applies the `max_depth` function to each group, and returns the results as a list.
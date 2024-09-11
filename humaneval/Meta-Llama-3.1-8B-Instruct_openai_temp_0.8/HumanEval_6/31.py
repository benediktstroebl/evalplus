```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input.
    For each group of parentheses, it calculates the maximum depth of nesting.
    
    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum depths of nesting for each group of parentheses.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def max_depth(s: str) -> int:
        """ Helper function to calculate the maximum depth of a single group of parentheses. """
        max_depth_so_far = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth_so_far = max(max_depth_so_far, current_depth)
            elif char == ')':
                if current_depth > max_depth_so_far:
                    max_depth_so_far = current_depth
                current_depth -= 1
        return max_depth_so_far

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    # Calculate and return the maximum depth of nesting for each group
    return [max_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and then calculates the maximum depth of nesting for each group using a helper function `max_depth`. It then returns a list of maximum depths for each group. The example usage demonstrates how to call the function and print the result.
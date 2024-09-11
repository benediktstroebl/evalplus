```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth_group(group: str) -> int:
        """ Helper function to calculate depth of a single group """
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth if max_depth <= current_depth else max_depth
    # Split the input string into groups
    groups = paren_string.split()
    return [max_depth_group(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` which splits the input string into groups and then calculates the maximum depth of each group using another helper function `max_depth_group`. The `max_depth_group` function iterates over each character in a group and updates the maximum depth when it encounters an opening parenthesis and decreases the current depth when it encounters a closing parenthesis. The function then returns the maximum depth if it is less than or equal to the current depth, meaning the parentheses are not properly closed. Finally, the script tests the function with the example input string.
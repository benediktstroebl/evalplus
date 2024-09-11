```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates and returns the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    def max_depth(s: str) -> int:
        """
        This is a helper function to calculate the maximum depth of a single group of parentheses.

        Args:
            s (str): A string of parentheses.

        Returns:
            int: The maximum depth of the string.
        """
        max_depth = 0
        current_depth = 0
        for c in s:
            if c == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif c == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()
    
    # Calculate the maximum depth for each group
    depths = [max_depth(group) for group in groups]
    
    return depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` which takes a string of groups of nested parentheses as input and returns a list of the deepest level of nesting for each group. The `max_depth` function is a helper function to calculate the maximum depth of a single group of parentheses. The script splits the input string into groups, calculates the maximum depth for each group, and returns the list of depths. The test at the end of the script checks that the function works correctly.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    def max_depth(group: str) -> int:
        """
        Calculate the maximum depth of nesting for a single group of parentheses.
        
        Args:
        group (str): A string containing a group of nested parentheses.

        Returns:
        int: The maximum depth of nesting for the group.
        """
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()
    # Use a list comprehension to calculate the maximum depth of nesting for each group
    return [max_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `max_depth` to calculate the maximum depth of nesting for a single group of parentheses. It then splits the input string into groups and uses a list comprehension to calculate the maximum depth of nesting for each group.
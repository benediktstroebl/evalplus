```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups of nested parentheses 
    separated by spaces. For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(group: str) -> int:
        """ Helper function to find the maximum depth of nesting for a given group. """
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and find the maximum depth for each group
    groups = paren_string.split()
    return [max_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `max_depth` to find the maximum depth of nesting for each group of parentheses. It iterates over the characters in the group, incrementing the depth when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum depth encountered during this process is returned as the maximum depth of nesting for the group. The main function `parse_nested_parens` splits the input string into groups and applies the `max_depth` function to each group to find the maximum depth of nesting.
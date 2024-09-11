```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the maximum depth of nesting for each group of parentheses.
    """
    def get_depth(s: str) -> int:
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    # For each group, calculate the maximum depth of nesting and add it to the result list
    return [get_depth(group) for group in groups]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `get_depth` to calculate the maximum depth of nesting for a single group of parentheses. It does this by iterating over the characters in the string, incrementing the current depth when encountering an open parenthesis and decrementing it when encountering a close parenthesis. The maximum depth encountered is kept track of and returned at the end.

The `parse_nested_parens` function then splits the input string into groups of parentheses using the `split` method, calculates the maximum depth of nesting for each group using the `get_depth` function, and returns the result as a list.
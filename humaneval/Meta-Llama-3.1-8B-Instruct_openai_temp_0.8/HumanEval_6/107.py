```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    def max_depth(parens: str) -> int:
        """Helper function to calculate the maximum depth of nesting for a given string."""
        depth = 0
        max_depth = 0
        for char in parens:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError("Unbalanced parentheses")
        return max_depth

    # Split the input string into groups and calculate the maximum depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups separated by spaces, and calculates the maximum depth of nesting for each group using a helper function `max_depth`. The function returns a list of integers representing the maximum depth of nesting for each group. The example usage at the end demonstrates how to call the function with the provided test case.
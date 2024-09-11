```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function parses a string of nested parentheses, separated by spaces, 
    and returns a list where each element represents the maximum level of nesting 
    for the corresponding group of parentheses.

    Args:
        paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
        List[int]: A list where each element represents the maximum level of nesting 
        for the corresponding group of parentheses.
    """
    def max_nesting(s: str) -> int:
        # Initialize the maximum nesting level and the current nesting level
        max_nest = 0
        nest = 0
        for char in s:
            if char == '(':
                nest += 1
                max_nest = max(max_nest, nest)
            elif char == ')':
                nest -= 1
        return max_nest

    # Split the input string into groups and calculate the maximum nesting level for each group
    return [max_nesting(group) for group in paren_string.split()]


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of maximum nesting levels for each group of parentheses. The function uses a helper function `max_nesting` to calculate the maximum nesting level for a given string of parentheses. The script then demonstrates how to use the function with an example input string.
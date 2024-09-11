```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups for nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting of parentheses for each group.

    Args:
    paren_string (str): A string of multiple groups for nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    def max_depth(s: str) -> int:
        """ Helper function to calculate the deepest level of nesting of parentheses. """
        max_level = 0
        current_level = 0
        for char in s:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    # Split the string into groups and calculate the maximum depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, we first define a helper function `max_depth(s)` to calculate the deepest level of nesting of parentheses for a given string `s`. We then use a list comprehension to split the input string into groups and calculate the maximum depth for each group. The result is a list of the deepest level of nesting of parentheses for each group.
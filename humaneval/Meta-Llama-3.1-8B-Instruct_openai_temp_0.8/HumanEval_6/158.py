```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_level(s: str) -> int:
        """ Find the maximum level of nesting in a given string. """
        max nive = 0
        cur_level = 0
        
        for char in s:
            if char == '(':
                cur_level += 1
                max nive = max(max nive, cur_level)
            elif char == ')':
                cur_level -= 1
        
        if cur_level!= 0:
            raise ValueError("Unbalanced parentheses in the input string")
        
        return max nive

    # Split the input string into groups and find the maximum level of nesting for each group
    return [max_level(group) for group in paren_string.split()]

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It first defines a helper function `max_level` that calculates the maximum level of nesting in a given string. The `parse_nested_parens` function then splits the input string into groups, calculates the maximum level of nesting for each group using `max_level`, and returns the results as a list.

The example usage at the end demonstrates how to use the `parse_nested_parens` function to calculate the maximum level of nesting for each group in the given input string.
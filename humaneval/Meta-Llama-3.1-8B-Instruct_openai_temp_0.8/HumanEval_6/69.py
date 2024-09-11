```python
from typing import List

def max_nesting_level(paren_string: str) -> int:
    """ Calculate the maximum nesting level of a single group of parentheses.
    
    Args:
    paren_string (str): A string representing a group of nested parentheses.
    
    Returns:
    int: The maximum nesting level of the parentheses.
    """
    stack = 0
    max_level = 0
    for char in paren_string:
        if char == '(':
            stack += 1
            max_level = max(max_level, stack)
        elif char == ')':
            stack -= 1
    return max_level


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): A string of groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of maximum nesting levels for each group of parentheses.
    """
    groups = paren_string.split()
    return [max_nesting_level(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines two functions: `max_nesting_level` and `parse_nested_parens`. The `max_nesting_level` function calculates the maximum nesting level of a single group of parentheses by iterating over the string and maintaining a stack. The `parse_nested_parens` function splits the input string into groups, calculates the maximum nesting level for each group using `max_nesting_level`, and returns a list of these levels.
```python
from typing import List

def max_parens_level(paren_group: str) -> int:
    """Calculate the maximum level of nesting for a single group of parentheses.
    
    Args:
    paren_group (str): A string of '(', ')', and spaces.
    
    Returns:
    int: The maximum level of nesting.
    """
    level = 0
    max_level = 0
    
    for char in paren_group:
        if char == '(':
            level += 1
            max_level = max(max_level, level)
        elif char == ')':
            level -= 1
            # We need to ensure we don't go below level zero
            level = max(level, 0)
    
    return max_level


def parse_nested_parens(paren_string: str) -> List[int]:
    """Parse a string representing multiple groups of nested parentheses separated by spaces.
    
    Args:
    paren_string (str): The input string.
    
    Returns:
    List[int]: A list of maximum levels of nesting for each group.
    """
    groups = paren_string.split()
    return [max_parens_level(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines two functions: `max_parens_level` calculates the maximum level of nesting for a single group of parentheses, and `parse_nested_parens` splits a string into groups and calculates the maximum level of nesting for each group. The test case at the end demonstrates the function's use.
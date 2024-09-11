```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum nesting level of parentheses in each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    results = []
    
    for group in groups:
        stack = []
        max_depth = 0
        
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                if stack:
                    stack.pop()
        
        results.append(max_depth)
    
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by splitting the input string into individual groups, then iterating over each group. It uses a stack to track the nesting level of parentheses and keeps track of the maximum depth seen so far. The maximum depth is then added to the results list. The function finally returns the list of maximum nesting levels for all groups.
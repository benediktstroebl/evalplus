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

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        level = 0
        max_level = 0
        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        result.append(max_level)
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by iterating over each group of parentheses in the input string. For each group, it keeps track of the current level of nesting and the maximum level of nesting seen so far. When it encounters an open parenthesis, it increments the level and checks if the current level is higher than the maximum level. When it encounters a close parenthesis, it decrements the level. Finally, it appends the maximum level to the result list.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of the deepest level of nesting 
    for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses 
            separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        result.append(max_depth)

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```

This script works by iterating over each character in each group of parentheses. When it encounters an open parenthesis, it increments the current depth. When it encounters a close parenthesis, it decrements the current depth. It keeps track of the maximum depth encountered for each group and appends this to the result list.
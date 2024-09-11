```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups of nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of spaces separated groups of nested parentheses.

    Returns:
        List[int]: A list of deepest nesting levels for each group of parentheses.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        nesting_level = 0
        max_level = 0

        for char in group:
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            elif char == ')':
                nesting_level -= 1

        result.append(max_level)

    return result

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of spaces separated groups of nested parentheses as input, splits the string into groups, and then for each group, it iterates through each character, keeping track of the current nesting level and the maximum nesting level encountered so far. Finally, it returns a list of maximum nesting levels for each group.
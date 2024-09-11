```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the maximum level of nesting for each group of parentheses.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_level = 0
        current_level = 0

        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1

        result.append(max_level)

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that splits the input string into groups of nested parentheses, then iterates over each group to find the maximum level of nesting. It uses a simple counter to keep track of the current level of nesting, incrementing it when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum level of nesting seen so far is updated whenever it encounters a deeper level of nesting. Finally, it returns a list of the maximum level of nesting for each group.
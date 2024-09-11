```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()
    results = []

    for group in groups:
        max_level = 0
        current_level = 0

        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1

        results.append(max_level)

    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```

This script uses a simple iterative approach to calculate the maximum depth of nesting for each group. It splits the input string into groups, then for each group, it iterates over each character, incrementing or decrementing the current level as it encounters opening or closing parentheses. The maximum level encountered during this process is stored and added to the results list.
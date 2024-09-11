```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list where each element is the maximum level of nesting for the corresponding group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of maximum level of nesting for each group.
    """
    groups = paren_string.split()
    max_levels = []

    for group in groups:
        levels = [0]  # To store the level of nesting for each pair of parentheses
        level = 0

        for char in group:
            if char == '(':
                level += 1
                levels.append(level)
            elif char == ')':
                level -= 1

        # The maximum level of nesting is the maximum level in the list
        max_levels.append(max(levels))

    return max_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by first splitting the input string into groups. Then for each group, it iterates over the characters, incrementing the level when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum level of nesting for each group is the maximum level in the list of levels.
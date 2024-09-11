```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting of parentheses for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting of parentheses for each group.
    """
    groups = paren_string.split()
    max_depths = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        max_depths.append(max_depth)

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Outputs: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces. It splits the string into groups, then for each group, it iterates over the characters to calculate the maximum depth of nesting. The maximum depths for all groups are returned as a list.

The script also includes a docstring with a description of the function, its parameters, and its return value. Additionally, it includes an example usage of the function.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses groups separated by spaces and returns a list of integers.
    Each integer represents the deepest level of nesting for the corresponding group.

    :param paren_string: A string of nested parentheses groups separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
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
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by splitting the input string into groups and then iterating over each character in each group. It keeps track of the current depth of nesting and updates the maximum depth whenever it encounters an open parenthesis. When it encounters a close parenthesis, it decreases the current depth. The maximum depth for each group is then added to the result list.
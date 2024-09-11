```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting of parentheses for each group.

    :param paren_string: A string of nested parentheses groups separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
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

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines the `parse_nested_parens` function, which splits the input string into groups, then iterates through each character in each group. It uses a stack to keep track of the current nesting depth, updating the maximum depth whenever it encounters an open parenthesis. Finally, it appends the maximum depth for each group to the results list and returns it.
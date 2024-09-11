```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers, where each integer represents the deepest level of nesting of parentheses in the corresponding group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting of parentheses in each group.
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

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by splitting the input string into groups of parentheses, then iterating over each group. For each group, it keeps track of the current depth of nesting and the maximum depth seen so far. It increments the current depth when it encounters an open parenthesis and decrements it when it encounters a close parenthesis. Finally, it appends the maximum depth seen for each group to the result list.
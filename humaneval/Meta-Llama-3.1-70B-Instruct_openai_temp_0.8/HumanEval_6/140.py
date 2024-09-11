```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string containing multiple groups of nested parentheses separated by spaces.
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


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
This script works by iterating over each character in each group of parentheses. It keeps track of the current depth (the number of open parentheses that have not been closed yet) and the maximum depth seen so far. When it encounters an open parenthesis, it increments the current depth and updates the maximum depth if necessary. When it encounters a close parenthesis, it decrements the current depth. After processing each group, it adds the maximum depth to the result list.
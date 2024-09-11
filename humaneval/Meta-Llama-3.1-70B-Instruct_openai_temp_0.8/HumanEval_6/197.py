```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers where each integer represents the deepest level of nesting of parentheses in each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers where each integer represents the deepest level of nesting of parentheses in each group.
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


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by splitting the input string into groups of parentheses, then iterating over each group to calculate the maximum nesting level. It uses a stack-based approach, where the `current_level` variable keeps track of the current nesting level, and the `max_level` variable keeps track of the maximum nesting level encountered so far. When a '(' character is encountered, the `current_level` is incremented, and when a ')' character is encountered, the `current_level` is decremented. The maximum level is updated whenever the `current_level` exceeds the `max_level`. Finally, the maximum level for each group is appended to the result list.
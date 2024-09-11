```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of nested parentheses separated by spaces
    :return: A list of integers representing the deepest level of nesting for each group
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

This script works by splitting the input string into groups of parentheses, then iterating over each group to calculate the maximum depth of nesting. It does this by keeping a running count of the current depth, incrementing it for each opening parenthesis and decrementing it for each closing parenthesis. The maximum depth seen so far is updated whenever the current depth exceeds it. Finally, the maximum depth for each group is added to the result list.
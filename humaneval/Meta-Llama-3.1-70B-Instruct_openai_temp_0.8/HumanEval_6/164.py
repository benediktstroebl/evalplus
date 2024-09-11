```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
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


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group. The function splits the input string into groups, then for each group, it iterates over the characters, keeping track of the current depth and the maximum depth encountered. Finally, it appends the maximum depth for each group to the result list.

In the example usage, the function is called with the string '(()()) ((())) () ((())()())' and the output is `[2, 3, 1, 3]`, which represents the deepest level of nesting for each group.
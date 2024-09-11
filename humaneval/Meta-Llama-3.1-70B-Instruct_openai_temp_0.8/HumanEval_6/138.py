```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string represented multiple groups for nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.
    """
    groups = paren_string.split()
    result = []

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

        result.append(max_depth)

    return result


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```
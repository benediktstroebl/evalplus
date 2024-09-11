```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of maximum nesting levels for each group.
    """
    result = []
    groups = paren_string.split()

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

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```

This Python script uses a stack-based approach to calculate the maximum nesting level of parentheses for each group. It splits the input string into groups, then iterates over each character in each group, updating the maximum depth as it encounters opening and closing parentheses. The final result is a list of maximum nesting levels for each group.
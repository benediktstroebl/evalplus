```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses in each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        stack = []
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                stack.pop()

        result.append(max_depth)

    return result


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by splitting the input string into groups of parentheses, and then for each group, it iterates over the characters. It uses a stack to keep track of the nesting level. When it encounters an open parenthesis, it pushes it onto the stack and updates the maximum depth if necessary. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack. The maximum depth for each group is then added to the result list.
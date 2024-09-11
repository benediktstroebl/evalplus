```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of integers representing the maximum depth of nesting for each group.
    """
    groups = paren_string.split()
    max_depths = []

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

        max_depths.append(max_depth)

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

In this script, we define the `parse_nested_parens` function that takes a string of nested parentheses groups as input. The function splits the input string into groups and then iterates over each group. For each group, it uses a stack to keep track of the nesting level of the parentheses. When it encounters an open parenthesis, it pushes it onto the stack and updates the maximum depth if necessary. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack. Finally, it adds the maximum depth for each group to the `max_depths` list and returns it.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the deepest levels of nesting
    deepest_levels = []

    for group in groups:
        # Initialize a stack to keep track of opening parentheses
        stack = []
        # Initialize the deepest level of nesting for the current group
        deepest = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the deepest level of nesting if necessary
                deepest = max(deepest, len(stack))
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()

        # Append the deepest level of nesting for the current group to the result list
        deepest_levels.append(deepest)

    return deepest_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits the string into groups, and for each group, it uses a stack to keep track of the opening parentheses and calculates the deepest level of nesting. The function returns a list of deepest levels of nesting for each group. The script includes a test case at the end to demonstrate the function's usage.
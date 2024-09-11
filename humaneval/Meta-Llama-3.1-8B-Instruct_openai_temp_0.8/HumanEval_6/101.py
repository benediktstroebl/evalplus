```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the maximum level of nesting for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses.

    Returns:
        List[int]: A list of integers representing the maximum level of nesting for each group.
    """

    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the maximum level of nesting for each group
    max_levels = []

    # Iterate over each group
    for group in groups:
        # Initialize a stack and the maximum level of nesting for the current group
        stack = []
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop the opening parenthesis from the stack
            elif char == ')':
                stack.pop()
                # If the stack is not empty, it means we are nesting parentheses, so increment the maximum level
                if stack:
                    max_level += 1
                # If the stack is empty, it means we are closing parentheses, so reset the maximum level
                else:
                    max_level = 0

        # The maximum level of nesting for the current group is the maximum level of the stack plus one
        max_levels.append(len(stack) + 1)

    return max_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first splits the input string into groups, then iterates over each group. For each character in the group, it checks if it's an opening or closing parenthesis and updates the maximum level of nesting accordingly. Finally, it returns a list of integers representing the maximum level of nesting for each group.
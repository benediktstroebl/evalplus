```python
from typing import List
import re
import collections

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting of parentheses in each group.
    """

    # Split the input string into groups of nested parentheses
    groups = re.split(r'\s+', paren_string)

    # Initialize a list to store the maximum depth of nesting for each group
    max_depths = []

    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the opening parentheses
        stack = []

        # Initialize the maximum depth of nesting for the current group
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth of nesting if the current depth is greater
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()

        # Append the maximum depth of nesting for the current group to the list
        max_depths.append(max_depth)

    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a stack to keep track of the opening parentheses in each group. It iterates over each character in the group, pushing opening parentheses onto the stack and popping corresponding closing parentheses from the stack. The maximum depth of nesting for each group is the maximum length of the stack at any point during the iteration. Finally, the script returns a list of the maximum depths of nesting for each group.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of the deepest level of nesting 
    for each group.

    :param paren_string: A string of multiple groups of nested parentheses 
                         separated by spaces.
    :return: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    max_depths = []  # Initialize a list to store the maximum depths

    for group in groups:
        stack = []  # Initialize a stack to keep track of the parentheses
        max_depth = 0  # Initialize the maximum depth for the current group

        for char in group:  # Iterate over each character in the group
            if char == '(':  # If the character is an opening parenthesis
                stack.append(char)  # Push it onto the stack
                max_depth = max(max_depth, len(stack))  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis
                stack.pop()  # Pop the corresponding opening parenthesis from the stack

        max_depths.append(max_depth)  # Append the maximum depth for the current group

    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
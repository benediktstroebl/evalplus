```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers where each integer represents the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces
    :return: A list of integers representing the deepest level of nesting for each group
    """
    groups = paren_string.split()  # Split the input string into groups
    result = []  # Initialize an empty list to store the results

    for group in groups:
        stack = []  # Initialize an empty stack to keep track of nesting levels
        max_depth = 0  # Initialize the maximum depth for the current group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis, push it to the stack
                stack.append(char)
                max_depth = max(max_depth, len(stack))  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis, pop from the stack
                if stack:  # Check if the stack is not empty to avoid index errors
                    stack.pop()

        result.append(max_depth)  # Append the maximum depth for the current group to the result list

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    result = []  # Initialize an empty list to store the results

    for group in groups:
        stack = []  # Initialize an empty stack for each group
        max_depth = 0  # Initialize the maximum depth for each group
        current_depth = 0  # Initialize the current depth for each group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis
                stack.append(char)  # Push it onto the stack
                current_depth += 1  # Increase the current depth
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis
                stack.pop()  # Pop the top of the stack
                current_depth -= 1  # Decrease the current depth

        result.append(max_depth)  # Append the maximum depth for each group to the result list

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
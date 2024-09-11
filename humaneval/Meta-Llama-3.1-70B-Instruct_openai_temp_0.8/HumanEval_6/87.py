```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting of parentheses in each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a stack to keep track of the opening parentheses
        stack = []

        # Initialize the maximum depth to 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth if necessary
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                stack.pop()

        # Append the maximum depth of the current group to the results list
        results.append(max_depth)

    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces as input, and returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group.

The function uses a stack to keep track of the opening parentheses in each group, and updates the maximum depth whenever it encounters a new opening parenthesis. The maximum depth of each group is then appended to the results list, which is returned at the end.

The script also includes a test case to demonstrate the function's usage.
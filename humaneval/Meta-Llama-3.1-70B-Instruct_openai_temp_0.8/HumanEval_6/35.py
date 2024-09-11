```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting of parentheses for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.
    """
    # Split the input string into a list of groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the nesting level
        stack = []

        # Initialize the maximum nesting level to 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack and update the maximum level
            if char == '(':
                stack.append(char)
                max_level = max(max_level, len(stack))
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                stack.pop()

        # Append the maximum nesting level for the current group to the results list
        results.append(max_level)

    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
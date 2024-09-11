Here's a Python solution that uses a stack to keep track of the opening parentheses:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of maximum nesting depths for each group of parentheses.
    """

    # Split the input string into groups
    groups = paren_string.split()
    result = []

    for group in groups:
        # Initialize stack to keep track of opening parentheses
        stack = []
        max_depth = 0

        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth if the stack size exceeds current max_depth
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()

        # Append the maximum nesting depth for the current group to the result list
        result.append(max_depth)

    return result

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
In this script, the function `parse_nested_parens` takes a string of nested parentheses as input, splits it into individual groups, and then iterates over each group to calculate the maximum nesting depth. The result is a list of maximum nesting depths for each group.
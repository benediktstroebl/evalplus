```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string representing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string into groups of nested parentheses
    groups = paren_string.split()

    def max_depth(group: str) -> int:
        # Initialize a stack to keep track of opening parentheses
        stack = []
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
                if stack:
                    stack.pop()

        return max_depth

    # Use a list comprehension to find the maximum depth of each group
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It splits the string into groups, and for each group, it uses a nested function `max_depth` to find the maximum depth of nesting. The maximum depth is then returned as a list of integers.

The `max_depth` function uses a stack to keep track of opening parentheses. When it encounters an opening parenthesis, it pushes it onto the stack, and when it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack. The maximum depth is updated each time a new opening parenthesis is pushed onto the stack.

Finally, the script tests the function with the example input '(()()) ((())) () ((())()())'.
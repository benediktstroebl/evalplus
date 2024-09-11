```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    It returns a list of the maximum depth of nesting of parentheses in each group.

    :param paren_string: A string of groups of nested parentheses separated by spaces.
    :return: A list of the maximum depth of nesting of parentheses in each group.
    """

    def max_depth(s: str) -> int:
        # Initialize a stack to keep track of the depth of nesting
        stack = 0
        max_stack = 0

        # Iterate over each character in the string
        for c in s:
            # If the character is an open parenthesis, push it onto the stack
            if c == '(':
                stack += 1
                max_stack = max(max_stack, stack)
            # If the character is a close parenthesis, pop the stack
            elif c == ')':
                stack -= 1

        # Return the maximum depth of nesting
        return max_stack

    # Split the input string into groups and return their maximum depths
    return [max_depth(group) for group in paren_string.split()]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `max_depth` that calculates the maximum depth of nesting of parentheses in a given string. It then uses this function in a list comprehension to calculate the maximum depth of nesting of parentheses for each group in the input string. The result is a list of maximum depths, which is returned by the main function `parse_nested_parens`.
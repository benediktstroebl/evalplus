from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Nested Parentheses
    # Input: a string containing some words and nested parentheses
    # Output: a list of integers representing the maximum number of nesting parentheses

    # Initialize the stack to keep track of the opening parentheses
    stack = []
    # Initialize the output to be the empty list
    output = []
    # Go through the string char by char
    for char in paren_string:
        # If char is an opening parenthesis
        if char == "(":
            # push to the stack
            stack.append(char)
        # If char is a closing parenthesis
        elif char == ")":
            # pop from the stack
            stack.pop()
        # If the string is empty
        if not stack:
            # push the current depth to the output
            output.append(len(stack))

    return output


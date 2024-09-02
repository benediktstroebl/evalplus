from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depths: List[int] = []

    # This is an example of the 'conceptual problem' of parsing a string to extract information from it.
    # In this problem, we're not looking to build a data structure, but to extract information from it.
    #
    # The reason why we're using a stack here is because we're trying to keep track of the number of
    # characters we've seen inside of each set of parentheses. When we reach a closing parenthesis,
    # we will pop off the stack and add the total number of characters in the characters seen
    # inside of that set of parentheses to the max_depths list.

    # Add a stack to keep track of the number of characters in each level
    stack = [0]
    # Iterate over each character in the string
    for char in paren_string:
        # Check if we're seeing a closing parenthesis
        if char == ")":
            # Pop off the stack and add the current number of characters in the stack to max_depths
            max_depths.append(stack.pop())
        # Otherwise, check if we're seeing an open parenthesis
        elif char == "(":
            # Add 1 to the stack
            stack.append(stack[-1] + 1)

    return max_depths

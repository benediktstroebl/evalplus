from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    n = len(paren_string)
    if n == 0:
        return []

    # initialize a stack to store the current level of nesting of each character
    stack = []

    # iterate through each character in the input string
    for c in paren_string:
        if c == '(':
            stack.append(0)
        else:
            stack.append(-1)

    # if the stack is empty, return an empty list
    if not stack:
        return []

    # initialize an empty list to store the maximum level of nesting of parentheses
    levels = []
    level = 0

    # iterate through each element in the stack
    for s in stack:
        # check if the current element is negative
        if s < 0:
            # if the current element is negative, it means that the nesting level has decreased
            level -= 1
        else:
            # if the current element is positive, it means that the nesting level has increased
            level += 1

        # append the current level of nesting to the list

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    """ALGORITHM"""
    # create an empty stack
    # iterate over the input string
    # if we see an open paren, append it to the stack
    # if we see a closed paren, pop the stack
    # the stack will have the indices of all open parens we've seen
    # the current open paren's index is the number of closed parens we've seen minus one
    # if we ever pop the stack and it's empty, raise a ValueError

    """BIG-O"""
    # time: O(n)
    # space: O(n)
    # where n is the length of the input string

    """EXAMPLES"""
    # parse_nested_parens('((()))')
    # parse_nested_parens('(()()) ((())) () ((())()())')

    if not isinstance(paren_string, str):
        raise TypeError("Input must be a string.")

    # create empty stack
    stack = []

    # iterate over the input string
    for i, char in enumerate(paren_string):

        # if we see an open paren, append it to the stack
        if char == "(":
            stack.append(i)

        # if we see a closed paren
        elif char == ")":
            # pop the stack
            if len(stack) == 0:
                raise ValueError("String has mismatched parentheses.")

            # current open paren's index is the number of closed parens we've seen minus one
            index_of_last_paren = stack.pop()
            # store level of nesting
            nesting_level = i - index_of_last_paren
            # append to output list
            stack.append(nesting_level)

    # if the stack is not empty, raise a ValueError
    if len(stack)!= 0:
        raise ValueError("String has mismatched parentheses.")

    # return the stack
    return stack


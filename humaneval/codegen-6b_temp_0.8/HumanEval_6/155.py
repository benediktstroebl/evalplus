from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    for character in paren_string:
        if character == '(':
            paren_stack.append(0)
        elif character == ')':
            start_index = len(paren_stack) - 1 - paren_stack[::-1].index(0)  # get the index of the first (
            end_index = len(paren_stack) - 1 - paren_stack[::-1].index(0, start_index + 1)  # get the index of the last )
            del paren_stack[end_index : start_index + 1]  # remove the closing ( from the stack
            paren_stack[end_index - 1] += 1  # increment the level of nesting

    return paren_stack


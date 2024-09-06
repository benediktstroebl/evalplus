from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # As part of preprocessing, we need to ensure that our string is properly balanced
    # and we have exactly one opening and closing parentheses per group.
    # However, this can be accomplished by a simple stack, where we push all opening parentheses,
    # and pop them when their corresponding closing parentheses are seen.
    # At the end, the size of the stack must be zero, and the size of the string must be a multiple
    # of two.
    opening = ['(', ')']
    count = 0
    for char in paren_string:
        if char in opening:
            count += 1
        else:
            count -= 1
        if count < 0:
            raise ValueError('Invalid string')
    if len(paren_string) % 2 != 0:
        raise ValueError('Invalid string')
    # Now that the string is properly balanced and has the appropriate structure, we can
    # parse it and extract the nested levels of parentheses.
    levels: List[int] = []
    current_level = 0
    for i, char in enumerate(paren

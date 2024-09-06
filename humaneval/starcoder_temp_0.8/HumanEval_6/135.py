from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Here we count the nesting level of each group.
    # When we see a close paren, we decrement the nesting level by 1.
    # When we see an open paren, we increment the nesting level by 1.
    # At the end, the nesting level of each group will be the deepest level of nesting.
    nesting_levels = [0] * len(paren_string)
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            nesting_levels[i] += 1
        else:
            nesting_levels[i - 1] -= 1
    return nesting_levels


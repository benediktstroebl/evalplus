from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # [0, 0, 0, 0]
    # []

    # [0, 0, 1, 0]
    # []

    # [0, 0, 1, 1]
    # []

    # [0, 0, 2, 2]
    # []

    # [0, 0, 2, 3]
    # []

    # [0, 0, 3, 4]
    # []

    # [0, 1, 4, 5]
    # []

    # [0, 1, 4, 6]
    # []

    # [0, 1, 5, 7]
    # []

    # [0, 1, 5, 8]
    # []

    # [0, 1, 6, 9]
    # []

    # [0, 2, 8, 10]
    # []

    # [0, 2, 8, 11]
    # []

    # [0, 2, 9, 12]
    # []

    # [0, 2, 9, 13]
    # []

    # [0, 3, 11, 14]
    # []

    # [0, 3, 11, 15]
    # []

    # [0, 3, 12, 16]
    # []

    # [0, 3, 12, 17]
    # []

    # [0, 4, 14, 18]
    # []

    # [0, 4, 14, 19]
    # []

    # [0, 4, 15, 20]
    # []

    # [0, 4, 15, 21]
    # []

    # [0, 4, 16, 22]
    # []

    # [0, 4, 1

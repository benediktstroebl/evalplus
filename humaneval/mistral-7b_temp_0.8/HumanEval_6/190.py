from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # todo: add unit tests for edge cases

    # 0. split input to groups
    parentheses_groups = [
        parentheses_string for parentheses_string in paren_string.split()
        if parentheses_string.strip()
    ]

    # 1. get number of nested parens for each group
    num_nested_parens = [
        len(paren_string) - len(paren_string.replace("()", "")) for paren_string in parentheses_groups
    ]

    return num_nested_parens

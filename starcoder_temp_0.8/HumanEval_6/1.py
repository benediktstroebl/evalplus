from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # store the level of nesting for each group of parentheses
    nested_level = [0] * len(paren_string)

    # nested level starts at 0 and increments by 1 for each (
    # and decrements by 1 for each )
    for idx, char in enumerate(paren_string):
        if char == '(':
            nested_level[idx] += 1
        elif char == ')':
            nested_level[idx] -= 1

    return nested_level

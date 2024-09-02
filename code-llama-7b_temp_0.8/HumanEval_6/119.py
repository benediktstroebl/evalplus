from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    # Whenever we encounter an open paren, increment the level
    # Whenever we encounter a closed paren, decrement the level
    # Whenever we encounter a new space, reset the level to 0
    return [max_level for _ in paren_string.split()]


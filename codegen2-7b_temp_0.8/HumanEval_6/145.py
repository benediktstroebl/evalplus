from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = []
    curr_level = 0
    for paren in paren_string:
        if paren == "(":
            curr_level += 1
        elif paren == ")":
            curr_level -= 1
            levels.append(curr_level)
    return levels


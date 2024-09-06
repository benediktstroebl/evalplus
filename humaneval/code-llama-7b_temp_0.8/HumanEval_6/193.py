from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    max_depth_rec = 0
    open_parens = 0
    output = []
    for ch in paren_string:
        if ch == "(":
            open_parens += 1
            max_depth_rec += 1
            if open_parens > max_depth:
                max_depth = open_parens
        elif ch == ")":
            open_parens -= 1
            max_depth_rec -= 1
        if open_parens == 0:
            output.append(max_depth)
            max_depth = 0
            max_depth_rec = 0
    return output


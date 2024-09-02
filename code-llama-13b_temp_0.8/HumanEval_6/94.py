from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    current_depth = 0
    res = []
    for paren in paren_string:
        if paren == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        else:
            current_depth -= 1
            if current_depth == 0:
                res.append(max_depth)
                max_depth = 0
    return res


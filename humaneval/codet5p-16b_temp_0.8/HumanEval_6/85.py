from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if paren_string.count("(")!= paren_string.count(")"):
        return []

    depth = 0
    max_depth = 0
    result = []
    for c in paren_string:
        if c == "(":
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif c == ")":
            depth -= 1
            if depth == max_depth - 1:
                max_depth = depth
        result.append(max_depth)

    return result


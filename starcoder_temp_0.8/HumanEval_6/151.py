from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    out = []

    for el in paren_string.split():
        depth = 0
        for c in el:
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            else:
                raise ValueError(f"Invalid char: {c}")
        out.append(depth)

    return out


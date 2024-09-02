from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    nested_groups = []
    for c in paren_string:
        if c == '(':
            depth += 1
            nested_groups.append(depth)
        elif c == ')':
            if nested_groups:
                depth = nested_groups.pop()
            else:
                depth -= 1
    return nested_groups


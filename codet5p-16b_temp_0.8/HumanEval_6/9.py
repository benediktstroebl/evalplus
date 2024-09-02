from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split()
    max_depth = 0
    for group in parens:
        depth = 0
        for char in group:
            if char == '(':
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                depth = 0
            if depth > max_depth:
                max_depth = depth
    return [max_depth] * len(parens)

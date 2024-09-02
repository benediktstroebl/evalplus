from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    current_depth = 0
    max_depth = 0

    for paren in paren_string:
        if paren == '(':
            current_depth += 1
        elif paren == ')':
            current_depth -= 1

        max_depth = max(max_depth, current_depth)

    return [max_depth] * len(paren_string)


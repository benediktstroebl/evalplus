from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_nesting_depth: int = 0
    current_depth: int = 0
    for ch in paren_string:
        if ch == "(":
            current_depth += 1
            max_nesting_depth = max(current_depth, max_nesting_depth)
        elif ch == ")":
            current_depth -= 1
    return [max_nesting_depth] * len(paren_string.split())


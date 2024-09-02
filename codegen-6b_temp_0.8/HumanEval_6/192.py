from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0

    def _parse_nested_parens(paren_string: str) -> List[int]:
        nonlocal depth
        depth += 1
        result = []
        for paren in paren_string:
            if paren == '(':
                result.extend(_parse_nested_parens(paren_string[1:]))
            elif paren == ')':
                return [depth] + result
            else:
                continue

    return _parse_nested_parens(paren_string)


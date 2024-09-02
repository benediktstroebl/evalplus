from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def _parse(paren_string: str) -> int:
        n = 0
        for c in paren_string:
            if c == "(":
                n += 1
            else:
                n -= 1
        return n

    return [_parse(paren_string)] + [_parse(paren_string) + _parse(paren_string) for _ in range(1, len(paren_string))

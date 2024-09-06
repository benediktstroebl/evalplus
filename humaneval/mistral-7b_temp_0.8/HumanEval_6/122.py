from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    open_parens, close_parens = 0, 0

    def max_level(string: str) -> int:
        for paren in string:
            if paren == '(':
                open_parens += 1
            elif paren == ')':
                open_parens -= 1
        return open_parens

    return [max_level(parentheses) for parentheses in paren_string.split(' ')]

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_parens(s):
        """ Count the nesting levels for the parentheses
        in the given string.
        """

        levels = 0
        for c in s:
            if c == '(':
                levels += 1
            elif c == ')':
                levels -= 1
        return levels

    result = []
    for group in paren_string.split():
        result.append(count_parens(group))
    return result


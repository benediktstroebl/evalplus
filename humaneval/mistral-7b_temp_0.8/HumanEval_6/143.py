from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _nested_parens_level(parentheses: str) -> int:
        """ Function to calculate the deepest level of nesting within a single group of parentheses.
        """
        counter = 0
        for p in parentheses:
            if p == '(':
                counter += 1
            elif p == ')':
                counter -= 1
        return counter

    return [_nested_parens_level(p) for p in paren_string.split()]

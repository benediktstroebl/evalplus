from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def get_nesting(paren_string: str) -> int:
        nesting = 0
        for char in paren_string:
            if char == '(':
                nesting += 1
            elif char == ')':
                nesting -= 1
            elif char == ' ':
                nesting += 1
        return nesting

    return [get_nesting(paren_string) for paren_string in paren_string.split()]

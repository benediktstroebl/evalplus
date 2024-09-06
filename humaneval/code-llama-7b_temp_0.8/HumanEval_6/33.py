from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def _check_paren_balance(open_paren_string: str) -> int:
        """
        Checks balance of parentheses.
        """
        level = 0
        for c in open_paren_string:
            if c == '(':
                level += 1
            else:
                level -= 1
        return level

    return [
        _check_paren_balance(open_paren_string)
        for open_paren_string in paren_string.split()
    ]


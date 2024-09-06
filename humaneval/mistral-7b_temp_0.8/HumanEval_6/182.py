from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def helper(paren_string: str) -> int:
        # base case
        if not paren_string:
            return 0
        if paren_string[0] == '(':
            return 1 + helper(paren_string[1:])
        return 0 + helper(paren_string[1:])
    return list(map(helper, paren_string.split()))


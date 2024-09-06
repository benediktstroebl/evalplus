from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def recurse(paren_string: str) -> int:
        # base case: exit if no parentheses left to parse
        if paren_string == "":
            return 0

        # try the best case, an open and close pair of parentheses.
        # if the parens are not well matched, we'll fall through to the "else" statement below.
        elif paren_string[0] == "(" and paren_string[-1] == ")":
            return 1 + recurse(paren_string[1:-1])

        # else we're left with a string of some sort (open parens, close parens, mixed).
        # if the string has any close parens, but no open ones, we return 0.
        # If the string has an open parenthesis, we return 1 + the result of calling
        # recurse on the remainder of the string.
        elif paren_string.count("(") > paren_string.count(")"):
            return 0
        elif paren_string.count("(") > 0:
            return

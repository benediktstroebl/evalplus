from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_count = [0]
    for paren_string in paren_string:
        if paren_string == "(":
            paren_count.append(paren_count[-1] + 1)
        elif paren_string == ")":
            paren_count.pop()

    return paren_count[

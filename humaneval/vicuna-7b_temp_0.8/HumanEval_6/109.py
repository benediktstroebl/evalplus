from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    count = [0] * 5

    for opening_paren in paren_string.strip('').split():
        for closing_paren in paren_string.strip('').split():
            if opening_paren == closing_paren:
                count[1] += 1
            else:
                if not count[0] == 0:
                    count[count[0] - 1] += 1
                count[1] += 1
                if not count[1] == 0:
                    count[count[1] - 1] += 1
    return count
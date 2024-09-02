from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_list = [0] * len(paren_string)
    max_nesting = 0

    for i, c in enumerate(paren_string):
        if c == "(":
            paren_list[i] = 1
            max_nesting += 1
        elif c == ")":
            if paren_list[i - 1] != 0:
                max_nesting -= 1
            paren_list[i] = -1

    return [max_nesting] + paren_list


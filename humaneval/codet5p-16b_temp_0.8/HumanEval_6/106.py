from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.split()
    nested_paren_levels = []
    for paren in paren_string:
        open_nesting = 0
        close_nesting = 0
        for c in paren:
            if c == '(':
                open_nesting += 1
            elif c == ')':
                close_nesting += 1
                if close_nesting > open_nesting:
                    open_nesting = 0
                    close_nesting = 0
        nested_paren_levels.append(open_nesting + close_nesting)
    return nested_paren_levels


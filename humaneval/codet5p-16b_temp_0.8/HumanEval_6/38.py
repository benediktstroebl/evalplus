from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens_nested_list = []

    groups = paren_string.split()
    for group in groups:
        open_parens = 0
        max_open_parens = 0
        close_parens = 0

        for paren in group:
            if paren == '(':
                open_parens += 1
                max_open_parens = max(max_open_parens, open_parens)
            else:
                open_parens -= 1
                close_parens += 1
                max_open_parens = max(max_open_parens, open_parens)
                if close_parens > max_open_parens:
                    max_open_parens = close_parens

        parens_nested_list.append(max_open_parens)

    return parens_nested_list


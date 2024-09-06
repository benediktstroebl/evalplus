from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    all_open_parens = list(filter(lambda x: x == '(', paren_string))
    all_close_parens = list(filter(lambda x: x == ')', paren_string))
    open_parens = []
    close_parens = []
    for element in all_open_parens:
        open_parens.append(all_open_parens.index(element))
    for element in all_close_parens:
        close_parens.append(all_close_parens.index(element))
    open_parens.sort(reverse=True)
    close_parens.sort(reverse=True)
    open_parens_end = []
    close_parens_end = []
    max_fringe = 0
    max_fringe_end = 0
    for index in open_parens:
        open_parens_end.append(index)
        max_fringe += 1
        if max_fringe > max_fringe_end:
            max_fringe_end = max_fringe
    for index in close_parens:
        if index > max_fringe_end:
            max_fringe_end = index
    max_fringe -= 1
    return max_fringe_end


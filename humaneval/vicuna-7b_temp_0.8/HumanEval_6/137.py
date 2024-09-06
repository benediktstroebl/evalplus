from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = []
    for opening, closing in (("()", "(")), ("[", "]"), ("{", "}")):
        levels.append((opening, closing, 0))
    for i, opening, closing in enumerate(levels[:-1]):
        for j, inner_opening, inner_closing in enumerate(levels[i+1:]):
            if levels[i][0] == opening and levels[j][0] == inner_opening:
                levels[i][1] = levels[j][1]
                levels[j][1] = 1
                del levels[i][j]
    return list(map(lambda x: x[1], levels))


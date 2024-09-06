from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_parens = 0
    deepest_parens = []
    for elem in paren_string.split(" "):
        if elem.count("(") > max_parens:
            max_parens = elem.count("(")
            deepest_parens = [max_parens]
        elif elem.count("(") == max_parens:
            deepest_parens.append(max_parens)
    return deepest_parens


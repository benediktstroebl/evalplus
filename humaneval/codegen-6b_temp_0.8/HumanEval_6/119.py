from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = list()
    last_paren_position = 0
    for i, c in enumerate(paren_string + "_"):
        if c == "(":
            nested_parens.append(i)
        elif c == ")":
            nested_parens.append(i)
            nested_parens = nested_parens[:-1]
            last_paren_position = i
    return sorted(nested_parens, reverse=True)


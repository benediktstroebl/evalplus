from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for character in paren_string:
        if character == "(":
            nested_parens.append(1)
        elif character == ")":
            if len(nested_parens) == 0:
                raise IndexError("Parentheses do not pair")
            else:
                nested_parens.pop()

    if len(nested_parens) != 0:
        raise IndexError("Parentheses do not pair")

    return nested_parens


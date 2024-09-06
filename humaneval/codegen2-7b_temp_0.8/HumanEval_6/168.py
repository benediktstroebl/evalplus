from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for paren_str in paren_string.split():
        if paren_str:
            if paren_str[0] == '(':
                nested_parens.append(
                    max(parse_nested_parens(paren_str[1:-1]))
                )
            else:
                nested_parens.append(len(paren_str))
    return nested_

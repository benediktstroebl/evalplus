from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if paren_string is None or len(paren_string) == 0:
        return []

    depths = []
    parentheses_depth = 0
    for parentheses in paren_string.split():
        if len(parentheses) == 0:
            continue

        for index, parentheses_char in enumerate(parentheses):
            if parentheses_char == '(':
                parentheses_depth += 1
            else:
                parentheses_depth -= 1

        depths.append(parentheses_depth)

    return depths

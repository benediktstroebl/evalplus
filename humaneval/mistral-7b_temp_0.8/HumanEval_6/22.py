from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_groups = paren_string.split(" ")
    result = []
    for paren_group in paren_groups:
        paren_depth = 0
        for paren in paren_group:
            if paren == "(":
                paren_depth += 1
            elif paren == ")":
                paren_depth -= 1
        result.append(paren_depth)
    return result


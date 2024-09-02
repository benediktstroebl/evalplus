from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []
    for group in groups:
        if ')' in group:
            nested = parse_nested_parens(group)
            for nested_item in nested:
                result.append(nested_item)
        else:
            result.append(1)
    return result


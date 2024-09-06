from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_strings = paren_string.split()
    nested_parens_count = 0
    result = []
    for paren_string in paren_strings:
        nested_parens_count = max(nested_parens_count, len(paren_string))
        result.append(nested_parens_count)
    return result


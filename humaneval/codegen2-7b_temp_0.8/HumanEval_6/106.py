from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    _ = paren_string.split(" ")
    max_nesting = 0
    max_nesting_level = 0
    max_nesting_level_index = 0
    for i, element in enumerate(_):
        if element == '(':
            nesting = 1
        else:
            nesting = -1
        if max_nesting_level < nesting:
            max_nesting = nesting
            max_nesting_level = nesting
            max_nesting_level_index = i
    return [max_nesting_level, max_nesting_level_index

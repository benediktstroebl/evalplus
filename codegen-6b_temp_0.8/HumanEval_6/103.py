from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    curr_level = 0
    for c in paren_string:
        curr_level += (c == '(') - (c == ')')
        max_level = max(max_level, curr_level)
    return parse_nested_parens_helper(paren_string, max_level, 0)


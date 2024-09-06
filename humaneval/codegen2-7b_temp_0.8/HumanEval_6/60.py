from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens_list = list(paren_string)
    max_nesting_level = 0
    nesting_level = 0
    for paren in parens_list:
        if paren == '(':
            nesting_level += 1
        elif paren == ')':
            nesting_level -= 1
            if nesting_level < 0:
                nesting_level = 0
        if nesting_level > max_nesting_level:
            max_nesting_level = nesting_level

    return [max_nesting_level

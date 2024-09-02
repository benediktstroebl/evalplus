from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_count = 0
    max_nesting_level = 0
    for char in paren_string:
        if char == '(':
            paren_count += 1
            max_nesting_level = max(paren_count, max_nesting_level)
        elif char == ')':
            paren_count -= 1
    return [max_nesting_level] + parse_nested_parens(paren_string[max_nesting_level + 1:]) if paren_count > 0

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    for paren in paren_string.split():
        cur_level = 0
        for i in range(len(paren)):
            if paren[i] == '(':
                cur_level += 1
            elif paren[i] == ')':
                cur_level -= 1
        max_level = max(cur_level, max_level)
    return [max_level] * len(paren_string

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for line in paren_string.split(' '):
        max_level, current_level = 0, 0
        for paren in line:
            if paren == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif paren == ')':
                current_level -= 1
            else:
                raise ValueError('"{paren}" is not a parenthesis.')
        result.append(max_level)
    return result


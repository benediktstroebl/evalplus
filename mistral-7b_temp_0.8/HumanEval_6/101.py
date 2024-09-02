from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_list = paren_string.split(' ')
    result = []
    for paren in paren_list:
        max_level = 0
        for i in range(len(paren)):
            if paren[i] == '(':
                max_level += 1
            elif paren[i] == ')':
                max_level -= 1
                if max_level < 0:
                    raise ValueError('Invalid paren string')
            result.append(max_level)
    return result

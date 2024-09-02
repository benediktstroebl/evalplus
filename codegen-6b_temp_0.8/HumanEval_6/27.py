from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_string = paren_string.replace('(', ' ( ')
    paren_string = paren_string.replace(')', ' ) ')
    paren_list = [paren_string.count(' ')]
    for char in paren_string:
        if char == '(':
            paren_list.append(paren_string.count('))'))
        if char == ')':
            paren_list.pop()
    return paren_list[::-1]


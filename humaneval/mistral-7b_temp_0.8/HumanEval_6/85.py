from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = []
    while paren_string:
        count = 0
        start = paren_string.find('(')
        end = paren_string.find(')')
        if end == -1:
            raise Exception('Unexpected end of string')
        nesting = end - start
        if nesting > count:
            count = nesting
        max_nesting.append(count)
        paren_string = paren_string[end+1:]
    return max_nesting


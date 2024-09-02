from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = []
    for element in paren_string.split(' '):
        if element.startswith('(') and element.endswith(')'):
            if '(' in element:
                parens.append(element.count('(') - element.count(')'))
            else:
                parens.append(1)
        else:
            parens.append(0)
    return parens


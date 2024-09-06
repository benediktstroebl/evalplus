from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_stack = []
    nesting = []

    for index, paren in enumerate(paren_string):
        if paren == '(':
            paren_stack.append(paren)
        elif paren == ')':
            if len(paren_stack) == 0:
                raise ValueError('Expected a left parenthesis, but got a right parenthesis at position {}'.format(index))
            else:
                paren_stack.pop()
        else:
            raise ValueError('Expected a left parenthesis or right parenthesis at position {}'.format(index))

        if len(paren_stack) > len(nesting):
            nesting.append(len(paren_stack))

    return nesting


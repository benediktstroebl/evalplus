from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()

    if paren_string.count('(')!= paren_string.count(')'):
        raise ValueError('Nested parens is not balanced')

    paren_string = paren_string.replace('(', '( ')
    paren_string = paren_string.replace(')',')')
    paren_string = paren_string.split()

    result = []
    for group in paren_string:
        group = group.strip()
        max_depth = 0
        for i, char in enumerate(group):
            if char == '(':
                max_depth += 1
            if char == ')':
                max_depth -= 1
            if max_depth == -1:
                break
        result.append(max_depth)
    return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    if paren_string[0] == '(' and paren_string[-1] == ')':
        return [1]

    paren_list = paren_string.split(' ')
    result = []

    for paren in paren_list:
        level = 0
        for c in paren:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1

            if level < 0:
                break

        result.append(level)

    return result

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_string = paren_string.replace(' ', '')
    nested_parens = []
    for i in range(1, len(paren_string)):
        nested_parens.append(0)
        for j in range(0, i):
            if paren_string[j] != '(':
                continue
            if paren_string[i] == '(':
                nested_parens[i] += 1
            elif paren_string[i] != ')':
                continue
            else:
                nested_parens[i] += nested_parens[j]
                break
    return nested_parens


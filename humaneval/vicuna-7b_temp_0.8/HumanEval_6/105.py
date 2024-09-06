from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for char in paren_string:
        if char == '(':
            result.append(0)
        elif char == ')':
            result[-1] += 1
        elif char == '':
            if not result[-1]:
                result.pop()
        else:
            result.append(int(char))
    return result


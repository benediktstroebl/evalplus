from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    assert paren_string != ''
    assert paren_string.count('(') == paren_string.count(')')
    res = []
    stack = []
    for i in range(0, len(paren_string)):
        if paren_string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                res.append(i - stack[-1])
    return res


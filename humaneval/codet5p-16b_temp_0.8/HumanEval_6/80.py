from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.split()
    stack = []
    ans = []
    for i, ele in enumerate(paren_string):
        if ele == '(':
            stack.append(i)
        elif ele == ')':
            j = stack.pop()
            ans.append(abs(i - j))
    return ans

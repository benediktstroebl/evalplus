from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = []
    for group in paren_string.split():
        stack = []
        nesting = 0
        for c in group:
            if c == '(':
                stack.append(c)
                nesting += 1
            elif c == ')':
                stack.pop()
                nesting -= 1
        max_nesting.append(nesting + 1)
    return max_nesting


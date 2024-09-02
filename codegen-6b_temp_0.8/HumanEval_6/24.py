from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_levels = []
    for paren in paren_string.split(' '):
        stack = []
        nesting = 0
        for char in paren:
            if char == '(':
                stack.append(1)
                nesting += 1
            elif char == ')':
                stack.pop()
                if not stack:
                    nesting_levels.append(nesting)
                else:
                    nesting -= 1
        if stack:
            nesting_levels.append(nesting)
    return nesting_levels


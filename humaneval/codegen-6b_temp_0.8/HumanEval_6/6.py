from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    level = 0
    nesting = []
    for paren in paren_string.split(' '):
        starting_depth = depth
        depth = 0
        for paren in paren:
            depth += 1
            if paren is '(':
                level += 1
            elif paren is ')':
                level -= 1
            if level == -1:
                nesting.append(starting_depth)
                break
    return nesting


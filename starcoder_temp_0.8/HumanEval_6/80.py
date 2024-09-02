from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths = []
    # print(paren_string)
    for i, c in enumerate(paren_string):
        if c == '(':
            depths.append(i)
        elif c == ')':
            depths.pop()
            depths.append(i)
    depths.append(len(paren_string))

    return [depth - depths[i-1] for i, depth in enumerate(depths[1:])]


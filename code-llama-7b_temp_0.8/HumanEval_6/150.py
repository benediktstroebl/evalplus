from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    output = []
    for i in paren_string.split():
        depth, depth_max = 0, 0
        for c in i:
            if c == '(':
                depth += 1
                depth_max = max(depth_max, depth)
            if c == ')':
                depth -= 1
        output.append(depth_max)
    return output


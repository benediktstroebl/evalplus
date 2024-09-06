from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split()
    max_depth = []
    for paren in paren_list:
        depth = 0
        for character in paren:
            if character == '(':
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                break
        max_depth.append(depth)
    return max_depth


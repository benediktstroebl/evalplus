from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []
    if paren_string[0]!= '(' or paren_string[-1]!= ')':
        raise ValueError("Must be surrounded by '(' and ')'")
    paren_list = []
    depth = 0
    for paren in paren_string[1:-1]:
        if paren == '(':
            depth += 1
        elif paren == ')':
            depth -= 1
        paren_list.append(depth)
    return paren_

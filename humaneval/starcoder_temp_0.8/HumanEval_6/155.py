from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_stack = []
    depth_list = []

    for paren in paren_string.split(" "):
        if paren == "(":
            paren_stack.append(paren)
        elif paren == ")":
            paren_stack.pop()
        if not paren_stack:
            depth_list.append(0)
        else:
            depth_list.append(len(paren_stack))

    return depth_list


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    out_list = []
    for paren in paren_string:
        if paren == "(":
            paren_stack.append(0)
        elif paren == ")":
            out_list.append(paren_stack.pop())
        if paren_stack:
            paren_stack[-1] += 1
    return out_list


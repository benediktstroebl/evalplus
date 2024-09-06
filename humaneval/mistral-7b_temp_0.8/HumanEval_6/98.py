from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_list = [int(p) for p in paren_string.split(' ') if p]
    stack = []
    for i, paren in enumerate(paren_list):
        if paren == 1:
            stack.append(i)
        elif paren == -1:
            stack.pop()
        if not stack:
            yield paren_list[i]


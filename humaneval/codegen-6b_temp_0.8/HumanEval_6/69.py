from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    max_depth = 0
    for paren in paren_string:
        if paren == '(':
            paren_stack.append(paren)
        else:
            if paren_stack:
                last_open_paren = paren_stack.pop()
                max_depth = max(max_depth, len(paren_stack))
            else:
                return None
    return max_depth


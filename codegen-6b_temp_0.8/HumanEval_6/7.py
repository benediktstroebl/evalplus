from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    level = 0
    for paren in paren_string:
        if paren == '(':
            level += 1
            paren_stack.append(level)
        elif paren == ')':
            if len(paren_stack) > 0:
                level = paren_stack.pop()
            else:
                level = 0
        else:
            continue
    return paren_stack


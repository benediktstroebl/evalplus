from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return
    paren_stack = []
    curr_level = 0
    for c in paren_string:
        if c == "(":
            paren_stack.append(curr_level)
            curr_level += 1
        else:
            if paren_stack:
                paren_stack.pop()
            if paren_stack:
                curr_level = max(curr_level, paren_stack[-1] + 1)
            else:
                curr_level = 0
    return paren_stack


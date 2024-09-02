from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level_stack = []
    max_level = -1
    out = []
    for char in paren_string:
        if char == '(':
            level_stack.append(char)
            max_level += 1
        elif char == ')':
            level_stack.pop()
            if max_level < len(level_stack):
                max_level = len(level_stack)
        if not level_stack:
            out.append(max_level)
            max_level = -1
    return out


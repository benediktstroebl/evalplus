from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []

    paren_stack = [0]  # index of the next open parenthesis
    level_stack = [0]  # nesting level of the last open parenthesis
    max_levels = []

    for paren in paren_string:
        if paren == '(':
            paren_stack.append(len(paren_string))
            level_stack.append(level_stack[-1] + 1)
        else:
            paren_stack.pop()
            level_stack.pop()
            if paren_stack:
                max_levels.append(level_stack[-1])

    max_levels.append(level_stack[-1])
    return max_levels


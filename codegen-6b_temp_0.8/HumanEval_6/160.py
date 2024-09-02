from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    nesting_levels = []
    for item in paren_string:
        level = 0
        if item == '(':
            level += 1
        elif item == ')':
            level -= 1
        stack.append(item)
        nesting_levels.append(level)
        if nesting_levels[-1] == 0:
            # If stack is empty at the end of parsing, we're done.
            break
    return nesting_levels


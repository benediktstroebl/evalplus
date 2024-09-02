from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level_stack = []
    deepest_level = 0
    max_level_stack = []
    for paren in paren_string:
        if paren == '(':
            level_stack.append(1)
            max_level_stack.append(level_stack[:])
        elif paren == ')':
            if level_stack:
                level_stack.pop()
            max_level_stack[-1] = level_stack[:]
    return [len(level) for level in max_level_stack]


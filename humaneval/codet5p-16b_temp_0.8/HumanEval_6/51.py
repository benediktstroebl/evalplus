from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_stack = []
    max_level = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            paren_stack.append(i)
            max_level = max(max_level, len(paren_stack))
        elif c == ')':
            if paren_stack:
                paren_stack.pop()
    return [max_level - i for i in range(1, max_level + 1)]
    # or
    # return [len(paren_stack) - i for i in range(1, len(paren_stack) + 1)]


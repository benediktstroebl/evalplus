from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    deepest = 0
    current = 0
    stack = []
    for char in paren_string:
        if char == '(':
            current += 1
            stack.append(current)
        elif char == ')':
            current -= 1
            if current == -1:
                deepest = max(deepest, len(stack))
    return [deepest, *stack

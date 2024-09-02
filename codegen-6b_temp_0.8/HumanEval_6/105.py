from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack: List[int] = []
    max_level: int = 0
    for s in paren_string:
        if s == '(':
            stack.append(1)
            max_level = max(max_level, len(stack))
        elif s == ')':
            popped = stack.pop()
            max_level = max(max_level, len(stack))
            while popped > 1:
                popped -= 1
                stack.pop()
        else:
            continue
    return max_level


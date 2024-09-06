from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    stack = []
    for char in paren_string:
        if char == '(':
            max_level += 1
            stack.append(max_level)
        elif char == ')':
            max_level -= 1
            if max_level == 0:
                stack.pop()
        elif char == '':
            if not stack:
                return []
            else:
                max_level = stack[-1]
        else:
            return []

    return [max_level for _ in stack]

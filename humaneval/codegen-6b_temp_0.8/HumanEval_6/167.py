from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    for paren in paren_string.split():
        if paren == '(':
            stack.append(0)
        elif paren == ')':
            last_paren_level = stack.pop()
            if not stack:
                stack.append(0)
            stack[-1] = max(stack[-1], last_paren_level + 1)
    return stack


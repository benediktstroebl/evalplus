from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = [0]
    stack = [0]
    for char in paren_string:
        if char == '(':
            stack.append(1)
            count[0] += 1
        elif char == ')':
            stack.pop()
            count[0] -= 1

        if stack[-1] == 0:
            count[0] -= 1
            while stack[-2] == 0:
                stack[-2] = stack.pop()
                count[0] -= 1

    return count


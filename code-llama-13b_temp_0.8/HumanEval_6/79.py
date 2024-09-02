from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    counter = 0
    result = []

    for char in paren_string:
        if char == '(':
            counter += 1
            stack.append(counter)
        elif char == ')':
            if len(stack) == 0:
                continue
            if stack[-1] == counter:
                stack.pop()
            counter -= 1
    result.append(counter)
    return result


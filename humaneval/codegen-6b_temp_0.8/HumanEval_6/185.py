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

    for index in range(len(paren_string)):
        current_level: int = 0

        if len(stack) == 0:
            stack.append(index)
        else:
            current_level = stack[-1]
            if paren_string[current_level] == '(':
                stack.append(index)
            elif paren_string[current_level] == ')':
                stack.pop()
                max_level = max(max_level, current_level + 1)

    stack = stack[::-1]
    max_level = len(stack)

    return [max_level, stack]


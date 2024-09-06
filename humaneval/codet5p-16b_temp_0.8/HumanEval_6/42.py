from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    current_level = 0
    max_level = 0
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_level += 1
            if current_level > max_level:
                max_level = current_level
        if char == ')':
            if len(stack) > 0:
                stack.pop()
                current_level -= 1
    return [max_level]


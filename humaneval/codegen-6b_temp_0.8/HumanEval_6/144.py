from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    index = 0
    max_level = 0

    while index < len(paren_string):
        symbol = paren_string[index]

        if symbol == "(":
            stack.append(index)
            max_level = max(max_level, len(stack) - 1)
        elif symbol == ")":
            stack.pop()

        index += 1

    return [max_level, len(stack)]


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    max_level = 0
    output = []

    for index, paren in enumerate(paren_string):
        if paren == "(":
            stack.append(paren)
            max_level = max(len(stack), max_level)
        elif paren == ")":
            if stack:
                stack.pop()
            else:
                max_level += 1

            if len(stack) == 0:
                output.append(max_level)
                max_level = 0

    return output


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    open_parens = 0
    stack = []
    output = []

    for char in paren_string:
        if char == "(":
            open_parens += 1
            stack.append(open_parens)
        elif char == ")":
            open_parens -= 1
            if open_parens == 0:
                max_level = stack.pop()
                output.append(max_level)

    return output


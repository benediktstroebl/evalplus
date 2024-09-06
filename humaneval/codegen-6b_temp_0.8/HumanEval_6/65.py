from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    nested_levels = []
    for i in range(len(paren_string)):
        c = paren_string[i]
        if c == "(":
            stack.append(i)
        elif c == ")":
            level = 0
            for j in range(len(stack)):
                level += paren_string[stack.pop()] == "("
            nested_levels.append(level)
    return nested_levels


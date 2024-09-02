from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    curr_depth = 0
    for s in paren_string:
        if s == "(":
            stack.append(curr_depth)
            curr_depth += 1
        elif s == ")":
            curr_depth -= 1
            if len(stack) == 0:
                raise Exception("Unbalanced parentheses")
            stack.pop()
    if len(stack) > 0:
        raise Exception("Unbalanced parentheses")
    return stack


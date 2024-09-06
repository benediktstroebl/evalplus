from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    paren_stack = []
    for c in paren_string:
        if c == "(":
            depth += 1
            paren_stack.append(c)
        elif c == ")":
            depth -= 1
            if depth < 0:
                raise ValueError("Missing closing parenthesis")
            paren_stack.pop()
        elif depth == 0 and c == " ":
            paren_stack.pop()
    return [depth] + paren_stack[::-1

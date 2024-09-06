from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    for paren_chunk in paren_string.split(" "):
        if paren_chunk == "(":
            paren_stack.append(len(paren_stack))
        elif paren_chunk == ")":
            if not paren_stack:
                raise RuntimeError("Not balanced parentheses")
            else:
                _ = paren_stack.pop()
    return paren_stack.copy

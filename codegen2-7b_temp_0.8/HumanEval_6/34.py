from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    for paren in paren_string.split():
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if stack:
                stack.pop()
        else:
            raise ValueError(f"Unrecognized paren: {paren}")
    if stack:
        raise ValueError("Mismatched parens")
    return stack

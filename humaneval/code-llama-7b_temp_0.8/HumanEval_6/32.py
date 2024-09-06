from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    paren_stack = []
    max_depth_count = []

    for paren in paren_string:
        if paren == "(":
            paren_stack.append(paren)
            max_depth = max(len(paren_stack), max_depth)
        elif paren == ")":
            if paren_stack:
                paren_stack.pop()
            else:
                raise ValueError(
                    f"Syntax error: More closing parentheses than opening parentheses. {paren_stack} {paren}"
                )

        if len(paren_stack) == 0:
            max_depth_count.append(max_depth)
            max_depth = 0
        else:
            max_depth = max(len(paren_stack), max_depth)

    if len(paren_stack) > 0:
        raise ValueError(
            f"Syntax error: More opening parentheses than closing parentheses. {paren_stack} {paren}"
        )

    return max_depth_count


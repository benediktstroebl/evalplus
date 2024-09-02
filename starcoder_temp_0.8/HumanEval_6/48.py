from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth_stack = []
    depth = 0
    result = []
    for paren in paren_string.split():
        if paren == "(":
            depth += 1
            depth_stack.append(depth)
        else:
            depth_stack.pop()
            if len(depth_stack) > 0:
                result.append(depth_stack[-1])
            else:
                result.append(0)

    return result

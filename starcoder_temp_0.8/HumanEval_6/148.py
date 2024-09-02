from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # the solution has O(n) runtime and O(1) space complexity
    stack = []
    max_depth = []
    for paren in paren_string.split():
        if paren == '(':
            stack.append(paren)
        else:
            stack.pop()
            max_depth.append(len(stack))
    return max_depth


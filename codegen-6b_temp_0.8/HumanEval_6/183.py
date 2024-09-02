from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = -1
    stack = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            stack.append(i)
        elif paren_string[i] == ")":
            if stack:
                stack.pop()
            if not stack:
                max_depth = max(max_depth, i)
            else:
                max_depth = max(max_depth, i - stack[-1])
    return max_depth + 1


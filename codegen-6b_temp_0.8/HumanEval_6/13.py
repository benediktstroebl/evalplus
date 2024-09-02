from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = [[1, [[1]]]]
    max_depth = 0
    for c in paren_string:
        if c == "(":
            new_depth, new_nested_parens = stack[-1][0] + 1, stack[-1][1] + [1]
            stack.append([new_depth, new_nested_parens])
        elif c == ")":
            stack.pop()
        else:
            stack[-1][1][-1] += 1

        max_depth = max(max_depth, new_depth)

    return [max_depth] * len(stack)


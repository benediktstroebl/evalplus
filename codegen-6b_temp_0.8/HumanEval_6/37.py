from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    depth = 0
    output = []
    for i in range(len(paren_string)):
        curr = paren_string[i]
        if curr == '(':
            stack.append(i)
        elif curr == ')':
            depth = max(depth, stack.pop() + 1)
            if len(stack) == 0:
                output.append(depth)
    return output


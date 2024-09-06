from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    """
    Brute force would be to calculate the depth of all the parentheses,
    and then use that depth to calculate the max depth of nesting.
    """
    # we can use a stack to keep track of the nesting
    stack = []
    max_depth = 0
    depth = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
            depth += 1
            # if this is the outermost level, add 1 since we add later
            if len(stack) == 1:
                max_depth += 1
        elif char == ')':
            stack.pop()
            depth -= 1
    # at this point, we need to know what the depth is of the last level
    max_depth += depth

    # we can now calculate the max depth with depth being the largest index
    # within the stack
    stack.append(i)
    depth = 0
    max_depth = 0
    for i in stack:
        depth += 1
        max_depth = max(max_depth, depth)
    return max_depth


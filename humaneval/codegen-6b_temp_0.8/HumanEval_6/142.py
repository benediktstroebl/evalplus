from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_stack = []
    stack_capacity = 0

    for i in paren_string:
        if i == '(':
            nesting_stack.append(0)
            stack_capacity += 1
        elif i == ')':
            # TODO: check for either empty or at end?
            nesting_stack.pop()
            stack_capacity -= 1

    # max nesting depth is the sum of all nesting depths
    return nesting_stack


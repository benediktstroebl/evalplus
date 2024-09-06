from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # using a stack to keep track of opening parentheses
    stack = []
    # output list
    output = []
    for char in paren_string:
        if char == '(':
            # stack.append(1)
            stack.append(char)
        else:
            # once we encounter a closing parenthesis
            if len(stack) > 0:
                # if stack is empty
                # this means we have unbalanced parentheses, ignore it and continue
                temp = stack.pop()
            # if stack is not empty
            # calculate max depth, pop the opening parentheses from stack, and store the maximum depth
            # in the output list
            output.append(len(stack))
    return output


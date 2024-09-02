from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split()
    output = [0] * len(paren_list)
    stack = []

    for i in range(len(paren_list)):
        if paren_list[i] == '(':
            stack.append(i)
        else:
            output[stack.pop()] = i - stack[-1]

    return output


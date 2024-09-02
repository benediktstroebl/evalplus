from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # DFS Search
    # DFS where we are recording the deepest level of nesting of parentheses
    # for each of the group of nested parentheses
    stack: List[int] = []
    groups = paren_string.split(' ')
    output = []

    for group in groups:
        stack.append(0)
        for paren in group:
            if paren == '(':
                stack[-1] += 1
            else:
                stack[-1] -= 1
        output.append(stack.pop())

    return output


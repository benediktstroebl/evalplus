from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_occurences = []

    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            paren_occurences.append(i)

    stack = [[0, 1]]
    for i in range(1, len(paren_occurences)):
        cur_level = paren_occurences[i] - stack[-1][1]
        stack.append([i, cur_level])

    return [max(i[1] for i in stack)]


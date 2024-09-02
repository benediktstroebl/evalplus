from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []

    paren_stack: List[int] = []  # index of current depth of nested parentheses
    groups: List[int] = []

    for i, paren in enumerate(paren_string):
        if paren == "(":
            paren_stack.append(i)
        elif paren == ")":
            paren_stack.pop()
        else:
            raise ValueError("Input string must consist of only parentheses")

        if not paren_stack:
            groups.append(i)

    return [groups[i + 1] - groups[i] for i in range(len(groups) - 1)]


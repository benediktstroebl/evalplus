from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    groups = paren_string.split(" ")
    group_stack = []

    for i in range(len(groups)):
        if groups[i] == "(":
            group_stack.append(i)
        else:
            group_stack.pop()
            if group_stack:
                print(group_stack[-1])
            else:
                print(i)


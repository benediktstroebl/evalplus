from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level = 0  # the current level of nesting
    max_level = 0  # the current max level of nesting
    paren_stack = []  # stores the number of opening and closing parentheses
    current_group_level = 0  # the current level of the most recently seen group
    for char in paren_string:
        if char == '(':
            paren_stack.append(('(', current_group_level))
            current_group_level += 1
        elif char == ')':
            paren_stack.append((')', current_group_level))
            current_group_level -= 1
            current_group_level -= 1
        max_level = max(max_level, current_group_level)
    # print(paren_stack)
    return list(reversed(list(range(max_level + 1))))


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    group_stack: List[int] = []
    current_group_size: int = 0
    group_sizes: List[int] = []

    for char in paren_string:
        if char == "(":
            current_group_size += 1
        elif char == ")":
            if current_group_size == 0:
                raise ValueError("Group size cannot be zero")
            current_group_size -= 1
            if not group_stack:
                group_sizes.append(current_group_size)
            elif group_stack[-1] < current_group_size:
                group_stack.append(current_group_size)
            else:
                group_sizes.append(group_stack.pop())

    if group_stack:
        raise ValueError(f"Unclosed groups: {group_stack}")

    return group_sizes


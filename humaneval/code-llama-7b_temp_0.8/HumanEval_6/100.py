from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    depth = 0
    output_list = []
    for char in paren_string:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1
        else:
            continue
    for char in paren_string:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        else:
            continue
        if depth == 0:
            output_list.append(max_depth)
            max_depth = 0
    return output_list


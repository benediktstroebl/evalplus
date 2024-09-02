from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parentheses_depths = []
    for group in paren_string.split():
        current_max_depth = 0
        i = 0
        while i < len(group):
            current_depth = 0
            if group[i] == '(':
                current_depth += 1
            elif group[i] == ')':
                current_depth -= 1
            if current_depth < 0:
                current_max_depth = max(current_max_depth, -current_depth)
            i += 1
        parentheses_depths.append(current_max_depth)
    return parentheses_depths


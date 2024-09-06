from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    list_of_paren_groups = paren_string.split()
    list_of_depths = []

    for paren_group in list_of_paren_groups:
        max_depth = 0
        cur_depth = 0
        for paren in paren_group:
            if paren == '(':
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)
            elif paren == ')':
                cur_depth -= 1
        list_of_depths.append(max_depth)
    return list_of_depths


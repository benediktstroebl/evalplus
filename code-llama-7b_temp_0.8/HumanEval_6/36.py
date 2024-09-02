from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Brute force approach
    max_depth = 0
    paren_list = []
    for group in paren_string.split():
        depth = 0
        for char in group:
            if char == '(':
                depth += 1
            if char == ')':
                depth -= 1
            if depth > max_depth:
                max_depth = depth
        paren_list.append(max_depth)
    return paren_list


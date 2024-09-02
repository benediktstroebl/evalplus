from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens_map = {}

    for char in paren_string:
        if char == '(':
            if nested_parens_map.get(len(nested_parens_map)) == len(nested_parens_map):
                nested_parens_map[len(nested_parens_map)] += 1
            else:
                nested_parens_map[len(nested_parens_map)] = 1
        elif char == ')':
            nested_parens_map[len(nested_parens_map) - 1] -= 1

    return nested_parens_map.values()


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nest_dict = {}
    nest_level = 1

    for c in paren_string:
        if c == '(':
            nest_level += 1
        elif c == ')':
            nest_level -= 1
            if nest_level == 0:
                nest_dict[nest_level] = 1
            else:
                nest_dict[nest_level] += 1

    return [nest_dict[key] for key in nest_dict]


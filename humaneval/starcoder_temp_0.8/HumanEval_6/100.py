from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Parse the parens string into a list of groups
    group_list = paren_string.split(" ")
    level_list = []
    for group in group_list:
        # Count how many parens are inside the group
        level = group.count("(") - group.count(")")
        level_list.append(level)

    return level_list


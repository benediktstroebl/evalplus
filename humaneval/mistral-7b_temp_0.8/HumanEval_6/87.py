from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    levels = []
    for parentheses_group in paren_string.split(" "):
        if parentheses_group == "":
            continue
        levels.append(len(paren_group_to_level(parentheses_group)) - 1)
    return levels


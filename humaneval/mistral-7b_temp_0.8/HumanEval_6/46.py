from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    list_of_levels = []
    for i in paren_string.split():
        if "(" not in i or ")" not in i:
            list_of_levels.append(1)
        else:
            level = 0
            for char in i:
                if char == "(":
                    level += 1
                if char == ")":
                    level -= 1
                if level < 0:
                    raise ValueError("found unpaired opening bracket")
            list_of_levels.append(level)
    return list_of_levels


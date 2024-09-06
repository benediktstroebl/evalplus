from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_levels = []

    for index in range(len(paren_string)):
        if paren_string[index] == "(":
            level = 1
            index += 1
            while index < len(paren_string) and paren_string[index] == "(":
                level += 1
                index += 1
            nested_levels.append(level)
        elif paren_string[index] == ")":
            level = 1
            index -= 1
            while level > 0:
                level -= 1
                index -= 1
    return nested_

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if len(paren_string) == 0:
        return []
    paren_string = paren_string.replace(" ", "")
    # assert paren_string.count("(") == paren_string.count(")"), "Parentheses don't match"
    max_level = 0
    result = []

    for paren_group in paren_string.split(" "):
        level = 0
        max_level_in_group = 0
        for char in paren_group:
            if char == "(":
                level += 1
                max_level_in_group = max(max_level_in_group, level)
            else:
                level -= 1
        result.append(max_level_in_group)
        max_level = max(max_level, max_level_in_group)

    return result


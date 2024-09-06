from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    # a list that will contain max levels of nesting for each group
    max_levels = []
    for group in paren_string.split():
        # Count the number of open parentheses and compare it to the current maximum level.
        # Increment the maximum level if necessary.
        level = 0
        for char in group:
            if char == "(":
                level += 1
            elif char == ")":
                level -= 1
            if level > max_level:
                max_level = level
        max_levels.append(max_level)
    return max_levels


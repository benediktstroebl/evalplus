from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # the idea is to count the left parens and when
    # you encounter a right paren, check if it is the right paren for the current level
    # if it is the right paren, the current max_level is max(max_level, current_level)
    # if it is not the right paren, update the current_level and continue
    max_level = 0
    current_level = 0
    levels = []
    for char in paren_string:
        if char == "(":
            levels.append(current_level)
            current_level += 1
        elif char == ")":
            current_level -= 1
            if current_level > max_level:
                max_level = current_level
    return levels


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # [0] for every open paren [1] create a new level
    # [2] If we have a closing paren check the previous level, and if that level is the deepest seen so far
    #     then add one to the deepest seen so far
    # [3] On every close paren, decrease the level by one
    max_level = 0
    level = 0
    depths = []
    for c in paren_string:
        if c == '(':
            level += 1
            if level > max_level:
                max_level = level
        elif c == ')':
            level -= 1
            if level == max_level:
                max_level += 1
        depths.append(max_level)
    return depths


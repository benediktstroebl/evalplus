from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_paren_levels = []
    queue = []

    for character in paren_string:
        if character == "(":
            queue.append([])
        elif character == ")" and len(queue) > 0:
            level = queue.pop()
            nested_paren_levels.append(len(level))
        else:
            pass

    return nested_paren_levels


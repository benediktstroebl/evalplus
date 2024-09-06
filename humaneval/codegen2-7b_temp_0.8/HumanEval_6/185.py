from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    assert len(paren_string) > 0
    nest_level, current_level = 0, 0
    for char in paren_string:
        if char == "(":
            current_level += 1
            nest_level = max(nest_level, current_level)
        else:
            current_level -= 1
    return [nest_level] + parse_nested_parens(paren_string[1:-1])


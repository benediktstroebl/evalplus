from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for index, paren_group in enumerate(paren_string.split()):
        current_level = 0
        for char in paren_group:
            if char == "(":
                current_level += 1
            elif char == ")":
                current_level -= 1
                if current_level < 0:
                    current_level = 0
        nested_parens.append(current_level)
    return nested_paren

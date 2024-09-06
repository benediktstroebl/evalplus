from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    output = []
    max_level = 0
    for group in paren_string.split():
        # reset max level for each group
        max_level = 0
        for char in group:
            if char == '(':
                max_level += 1
            elif char == ')':
                max_level -= 1
        output.append(max_level)
    return output


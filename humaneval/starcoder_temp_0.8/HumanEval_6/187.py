from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    output = []

    for group in paren_string.split():
        open_paren_count = 0
        max_depth = 0

        for char in group:
            if char == '(':
                open_paren_count += 1
                max_depth = max(max_depth, open_paren_count)
            else:
                open_paren_count -= 1
                max_depth = max(max_depth, open_paren_count)

        output.append(max_depth)

    return output

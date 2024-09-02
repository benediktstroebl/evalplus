from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_levels = []

    def get_nesting_level_of_paren(paren_string: str) -> int:
        nesting_level = 0
        open_paren_count = 0
        close_paren_count = 0

        for char in paren_string:
            if char == '(':
                open_paren_count += 1
            elif char == ')':
                close_paren_count += 1

            if open_paren_count > close_paren_count:
                nesting_level += 1
            elif open_paren_count < close_paren_count:
                nesting_level -= 1

        return nesting_level

    for paren_string in paren_string.split():
        nesting_levels.append(get_nesting_level_of_paren(paren_string))

    return nesting_levels


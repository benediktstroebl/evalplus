from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level_of_nesting = 0
    paren_strings = paren_string.split()
    for paren_string in paren_strings:
        current_max_level_of_nesting = 0
        current_nesting = 0
        for char in paren_string:
            if char == '(':
                current_nesting += 1
                current_max_level_of_nesting = max(current_max_level_of_nesting, current_nesting)
            if char == ')':
                current_nesting -= 1
        max_level_of_nesting = max(max_level_of_nesting, current_max_level_of_nesting)
    return max_level_of_nesting


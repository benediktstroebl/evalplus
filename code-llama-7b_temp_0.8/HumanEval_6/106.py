from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # First, we are going to split the string into a list of substrings
    # We will count the left and right parenthesis in each substring to find the max nesting level
    left_parens = 0
    right_parens = 0
    max_nesting_level = 0
    max_nesting_level_substrings = []
    string_list = paren_string.split()

    for substring in string_list:
        left_parens = 0
        right_parens = 0
        for char in substring:
            if char == '(':
                left_parens += 1
            if char == ')':
                right_parens += 1
        if left_parens > max_nesting_level:
            max_nesting_level = left_parens
        if right_parens > max_nesting_level:
            max_nesting_level = right_parens
        if left_parens == right_parens:
            max_nesting_level_substrings.append(left_parens)
    return max_nesting_level_substrings


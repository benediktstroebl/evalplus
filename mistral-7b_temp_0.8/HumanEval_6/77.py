from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # parentheses_levels_array is a list that is as long as there are strings in the input string
    # and it holds the maximum nesting level for each of the strings
    parentheses_levels_array = []

    # parentheses_level_counter is a counter that is used to track the maximum nesting level
    # for each of the strings in the input string
    parentheses_level_counter = 0

    # paren_string_counter is used to track the current index of the input string
    paren_string_counter = 0

    # while paren_string_counter is smaller than the length of the input string, continue iterating through the
    # strings
    while paren_string_counter < len(paren_string):
        # if the current character in the input string is a parenthesis, either left or right, then increase
        # the parentheses_level_counter by one
        if paren_string[paren_string_counter] == '(':
            parentheses_level_counter += 1
        # otherwise, if the current character in the

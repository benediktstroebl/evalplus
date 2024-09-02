from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse_string_to_list(paren_string: str) -> List[str]:
        """ Takes a string and converts it to a list of sub-strings. """
        return [s for s in paren_string.split()]

    def parse_string_to_int(parent_string: str) -> int:
        """ Takes a string and returns its int value. """
        return int(parent_string)

    nested_parens = []

    paren_list = parse_string_to_list(paren_string)
    for paren_string in paren_list:
        level_of_nesting = 0
        for char in paren_string:
            if char == "(":
                level_of_nesting += 1
            elif char == ")":
                level_of_nesting -= 1
        nested_parens.append(level_of_nesting)

    return nested_parens


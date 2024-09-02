from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def get_deepest_level(paren_string: str) -> int:
        """This method returns the deepest level of nesting of parentheses for a given string
        >>> get_deepest_level('(()())')
        2
        """
        level = 0
        for char in paren_string:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1

        return level

    return [get_deepest_level(group) for group in paren_string.split()]


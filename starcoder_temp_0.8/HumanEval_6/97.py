from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _parse_nested_parens(string: str) -> int:
        if len(string) < 2:
            return 0

        if string[0]!= "(" or string[-1]!= ")":
            raise ValueError("Parenthesis string should be of form ((()))")

        count_of_open_parens = 0
        level = 0
        for char in string:
            if char == "(":
                count_of_open_parens += 1
                if count_of_open_parens > level:
                    level = count_of_open_parens
            elif char == ")":
                count_of_open_parens -= 1
        return level

    return [_parse_nested_parens(paren_group) for paren_group in paren_string.split()]


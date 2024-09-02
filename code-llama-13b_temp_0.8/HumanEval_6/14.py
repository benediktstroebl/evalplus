from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _get_deepest_paren_level(s: str) -> int:
        current_paren_level = 0
        max_paren_level = 0
        for char in s:
            if char == "(":
                current_paren_level += 1
                max_paren_level = max(max_paren_level, current_paren_level)
            elif char == ")":
                current_paren_level -= 1
        return max_paren_level

    return list(map(_get_deepest_paren_level, paren_string.split()))


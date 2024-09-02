from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _parse(substrings: List[str]) -> List[int]:
        max_level = 0
        for sub in substrings:
            max_level = max(max_level, len(sub) - 1)
        return max_level

    return _parse(parse_nested_parens(paren_string))


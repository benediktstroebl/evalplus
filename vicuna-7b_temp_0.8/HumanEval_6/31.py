from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_levels(parentheses: List[str]) -> int:
        levels = 0
        for i, subparens in enumerate(parentheses):
            levels += count_levels(subparens)
        return levels

    return list(map(count_levels, paren_string.split()))

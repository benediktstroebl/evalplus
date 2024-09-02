from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_max_nesting(nested_parens: List[str]) -> int:
        count = 0
        nesting_level = 0
        for inner_parens in nested_parens:
            count += nesting_level
            nesting_level = nesting_level + 1
        return count

    return count_max_nesting(List(paren_string.split()))
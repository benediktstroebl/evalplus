from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def flatten(lst):
        return [item for sublist in lst for item in sublist]

    def count_nesting(lst):
        return len(lst) * 2

    return flatten(list(map(count_nesting, parse_nested_parens(paren_string))))

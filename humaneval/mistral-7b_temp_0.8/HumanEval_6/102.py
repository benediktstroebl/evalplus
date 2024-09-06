from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # This function does not use recursion, so that it is easier to test.
    if not paren_string:
        return []

    # Split the input string into groups of parentheses and spaces
    paren_groups = paren_string.split()
    paren_counts = [parse_paren_group(group) for group in paren_groups]
    return paren_counts


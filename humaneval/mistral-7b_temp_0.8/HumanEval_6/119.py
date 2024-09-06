from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if paren_string == '':
        return []

    # Parse the input into a list of groups.
    groups = paren_string.split(' ')

    # Iterate through each group and get its nested parens count.
    return [get_parens_count(group) for group in groups]


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # First sort out the case where paren_string is just a string of no parens
    if not paren_string:
        return []

    # Start with the groups that don't have parens
    groups = [x for x in paren_string.split(' ') if x[0] != '(' and x[-1] != ')']

    # Now add the groups that have parens to the list of groups we care about.
    groups = [add_parens(g) for g in groups]

    # Sort the groups by the longest group to the shortest group
    groups.sort(key=lambda x: x[1] - x[0], reverse=True)

    # The final groups are the groups in sorted order
    return [len(g) for g in groups]


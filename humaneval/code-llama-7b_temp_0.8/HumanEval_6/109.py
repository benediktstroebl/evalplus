from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # The counter for the current "group"
    curr_group_count = 0
    # The counters for all the groups
    group_counts = []
    for ch in paren_string:
        if ch == '(':
            curr_group_count += 1
        if ch == ')':
            curr_group_count -= 1
        # If the current group count is zero, that means we are at the end of a group
        if curr_group_count == 0:
            # Record the max count for this group
            group_counts.append(max(group_counts or [0]))
    return group_counts


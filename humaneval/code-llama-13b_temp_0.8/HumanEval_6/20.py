from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # depth tracking
    max_depth = 0
    curr_depth = 0

    # output
    res = []

    # parses each group
    for group in paren_string.split():
        # resets the depth
        curr_depth = 0
        for paren in group:
            # increase the depth
            if paren == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            # decrease the depth
            elif paren == ')':
                curr_depth -= 1

        # appends the maximum depth to the output
        res.append(max_depth)

    return res


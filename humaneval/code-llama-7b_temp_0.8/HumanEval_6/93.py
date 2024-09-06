from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # find all open and close parens indices
    open_paren_indices = [i for i, c in enumerate(paren_string) if c == '(']
    close_paren_indices = [i for i, c in enumerate(paren_string) if c == ')']

    # initialize deepest_nest_count_at_each_position variable
    deepest_nest_count_at_each_position = [-1] * len(paren_string)

    # iterate over open and close paren indices
    for i in range(len(open_paren_indices)):
        start, end = open_paren_indices[i], close_paren_indices[i]
        # if start index is 0, the current paren group is on the leftmost.
        if start == 0:
            # maximum nesting level at start position is the current end index
            deepest_nest_count_at_each_position[start] = end
            # maximum nesting level at end position is current end index too
            deepest_nest_count_at_each_position[end] = end
        # if end index is -1, the current paren group is on the rightmost.
        elif end == -1:
            # maximum nesting level at start position is the current start index
            deepest_nest_count_at_each_position[start] = start
            # maximum nesting level at end position is current start index too
            deepest_nest_count_at_each_position[end] = start
        # if it is neither -1 nor 0, then it is a paren group in the middle of the string.
        else:
            # maximum nesting level at start position is the start index
            deepest_nest_count_at_each_position[start] = start
            # maximum nesting level at end position is end index
            deepest_nest_count_at_each_position[end] = end
            # maximum nesting level at positions between start and end is the difference between start and end index
            for position in range(start + 1, end):
                deepest_nest_count_at_each_position[position] = end

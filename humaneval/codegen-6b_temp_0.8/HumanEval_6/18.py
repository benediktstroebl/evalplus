from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Your code here.
    max_depth = max_depth_counter = 0
    depth_n_parens = []
    paren_list = []

    for char in paren_string:

        if char == '(':
            max_depth_counter += 1
            depth_n_parens.append(max_depth_counter)
            max_depth = max(max_depth, max_depth_counter)

        if char == ')':
            max_depth_counter -= 1
            depth_n_parens.append(max_depth_counter)
            max_depth = max(max_depth, max_depth_counter)

        if max_depth_counter == 0:
            paren_list.append(depth_n_parens)
            max_depth_counter = depth_n_parens = 0
            depth_n_parens = []

    # remove leftover depth_n_parens elements.
    while depth_n_parens:
        paren_list.append(depth_n_parens)
        depth_n_parens = []

    return paren_list


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # If we are at a pair of nested parenthesis then increase depth counter by 1
    depth_counter = 0
    index = 0
    # This list will be populated with the index positions of the nested parenthesis
    nested_parens = []
    # This list will be populated with the last index position of each nested group
    last_deeper_index = []
    while index < len(paren_string):
        if paren_string[index] == '(':
            depth_counter += 1
            # Add the index of the current group to the list of nested parentheses
            nested_parens.append(index)
            # If this group is not the last in the string, then we want to store the last index of this group
            if index + 1 < len(paren_string):
                last_deeper_index.append(index)
        elif paren_string[index] == ')':
            depth_counter -= 1
            # If this group is not the last in the string, then we want to store index of last position of this group
            if index + 1 < len(paren_string):
                last_deeper_index.append(index)
        index += 1
    # For each position we found in the nested parentheses, we want to calculate the depth of nesting
    # The depth is the index of the last position of a nested group minus the index of the first nested group
    last_deeper_index.reverse()
    for i in range(1, len(last_deeper_index)):
        last_deeper_index[i] -= last_deeper_index[i - 1]
    # For each index position of a nested group, we want to find the depth of nesting by taking
    # the max of the depth of nesting of a nested group at that index and the depth of nesting of
    # the current group we're looking at.
    depth = [None] * len(paren_string)
    for i, position in enumerate(nested_parens):
        depth[position] = depth_counter
    for i, position in enumerate(last_deeper_index):
        depth[position] = max(depth[position], depth_counter)
    return depth


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Keep track of how many layers we're at
    depth = 0
    # The start index of the bracket
    start_idx = 0
    # The map of depth to index, where depth is 0 for a) the unbracketed part and 1+ for a) the bracketed part
    depth_map = {0: 0}
    # The maximum depth we've seen
    max_depth = 0
    # The result
    result = []

    # We iterate over the string, so we can always find the next index in paren_string
    for idx, c in enumerate(paren_string):
        if c == '(':
            depth += 1
            # If we've seen a new maximum depth of nesting, we have to check for a previous maximum depth that was lower
            if depth > max_depth:
                max_depth = depth
                depth_map[depth] = idx
            # If we're already in the maximum depth, we've reached the start of the next group of brackets
            elif depth == max_depth:
                depth_map[depth] = idx
        elif c == ')':
            depth -= 1
            # If we've seen a new maximum depth of nesting, we have to check for a previous maximum depth that was lower
            if depth > max_depth:
                max_depth = depth
                depth_map[depth] = idx
            # If we're already in the maximum depth, we've reached the end of the previous group of brackets
            elif depth == max_depth:
                depth_map[depth] = idx
        else:
            # We only care about the part of the string that is between parentheses, so we zero out the depth for the
            # part of the string before the first opening bracket and after the last closing bracket
            depth_map[0] = 0
            depth_map[max_depth + 1] = len(paren_string)

    # We iterate over the depth map to get the start index and depth of each group
    for depth, start_idx in depth_map.items():
        # We add the number of layers to the result
        result.append(depth)
        # We now iterate over the depths backwards to find the first index of the next
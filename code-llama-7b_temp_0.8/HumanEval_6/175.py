from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Keep track of the maximum nesting level so far and the index of the current group
    max_depth = -1
    curr_depth = 0
    curr_group_start = 0
    # List to store the output
    output_list = []
    # Iterate over the characters in the string
    for i, paren in enumerate(paren_string):
        if paren == '(':
            # Keep track of the current depth of nesting
            curr_depth += 1
            # If the current level of nesting is higher than the maximum seen so far, update the maximum
            if curr_depth > max_depth:
                max_depth = curr_depth
        elif paren == ')':
            # Keep track of the current depth of nesting
            curr_depth -= 1
        # If the nesting level is 0, we have encountered a group's end
        if curr_depth == 0:
            # Append the maximum depth seen so far for the group
            output_list.append(max_depth)
            # Reset the maximum depth
            max_depth = -1
            # Reset the depth and set the start index of the next group
            curr_depth = 0
            curr_group_start = i + 1
    return output_list


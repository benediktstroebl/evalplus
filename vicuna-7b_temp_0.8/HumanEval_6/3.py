from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Add 1 to the nesting level for each opening paren in the input string
    nesting_levels = [1 + nesting_level for nesting_level in paren_string]

    # Initialize a list to store the maximum nesting level for each group
    nesting_levels_max = [0] * len(nesting_levels)

    # Loop over the input string, starting from the second group (as the first group is just the input string itself)
    for i in range(1, len(nesting_levels)):
        # Get the nesting level of the current group
        nesting_level = nesting_levels[i]

        # If the current nesting level is greater than the maximum nesting level for this group, update the maximum
        if nesting_level > nesting_levels_max[i - 1]:
            nesting_levels_max[i - 1] = nesting_level

    # Return the list of maximum nesting levels for each group
    return nesting_levels_max


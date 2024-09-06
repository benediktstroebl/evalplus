from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # for each character, keep track of the level of nesting; the nesting level of a character is the
    # highest level of nesting that it can reach by descending to the left or right if necessary
    depth = 0
    nesting_levels = [0] * len(paren_string)
    for i, char in enumerate(paren_string):
        if char == '(':
            depth += 1
            nesting_levels[i] = depth
        elif char == ')':
            depth -= 1

    max_depth = 0
    # for each index in the string, find the max depth that the index can reach
    for i, char in enumerate(paren_string):
        if char == '(':
            max_depth = max(max_depth, nesting_levels[i])
        elif char == ')':
            max_depth = max(max_depth, nesting_levels[i])

    return [max_depth] + nesting_levels


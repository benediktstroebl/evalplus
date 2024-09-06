from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    current_depth = 0
    for char in paren_string:
        if char == '(':
            current_depth += 1
        elif char == ')':
            current_depth -= 1
        max_depth = max(max_depth, current_depth)
    return max_depth * [0]

    # Iterate through the string and calculate the depth of each group - starting with the outermost groups
    # Time - O(n)
    # Space - O(n)
    # n is the length of the string


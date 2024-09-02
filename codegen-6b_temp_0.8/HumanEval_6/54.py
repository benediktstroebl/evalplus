from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Track the depth of the nesting
    depth = 0
    # Track the current nesting level
    current_level = 0
    # Track the max depth of nesting
    max_level = 0

    # Track the depth of the nesting
    for i in range(len(paren_string)):
        # Traverse through the string to see if we have a balanced expression or not.
        if paren_string[i] == '(':
            depth += 1
            current_level += 1
            if current_level > max_level:
                max_level = current_level
        elif paren_string[i] == ')':
            depth -= 1
            current_level -= 1
        # Once we see a balanced expression, we will compute the max depth.
        if depth == 0:
            current_level = 0

    return [max_level, *depth]


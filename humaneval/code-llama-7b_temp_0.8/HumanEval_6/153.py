from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    res = []
    # Loop through all groups
    for group in paren_string.split():
        # Initialize maximum level of nesting for this group
        max_level = 0
        # Loop through all characters in this group
        for char in group:
            # If character is '(' then increase current level, else decrease current level
            if char == '(':
                max_level += 1
            else:
                max_level -= 1
        # Append maximum level of nesting for this group
        res.append(max_level)

    return res


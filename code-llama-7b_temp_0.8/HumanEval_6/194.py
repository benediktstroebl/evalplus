from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    # We can keep track of the current level of nesting
    # if we count the number of open parentheses we have encountered so far.
    level = 0
    for char in paren_string:
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        if level < 0:
            # If we find a closing parenthesis, but we have a
            # negative level, it means that there was an unbalanced
            # opening parenthesis earlier in the string.
            return []
        # We can check the level to see if it is a new maximum.
        if level == 0:
            result.append(level)
    # We can also handle the edge case where the string does not
    # have balanced parentheses.
    return [] if level > 0 else result


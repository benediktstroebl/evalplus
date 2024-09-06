from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # We will start with the first group, then we'll iterate through this from the beginning to the end.
    # If the next level is a closing paren, we print the depth of the previous level
    # If the next level is a opening paren, we will print the depth of the previous level + 1
    # Finally, we will print the depth of the last level.
    parens = []
    depth = 0
    for group in paren_string.split():
        if group == '(':
            parens.append(depth)
            depth += 1
        elif group == ')':
            depth -= 1
            parens.append(depth)
        # This will not include the last level, since there's no () to close them.
        # It will only check the previous indices, so we could have (()(()))
        # We'll manually add an extra 1 in the first index, so we know we have a nested paren,
        # since there is a closing paren before the first level.
        elif group != ',':
            parens.append(depth)
    return parens


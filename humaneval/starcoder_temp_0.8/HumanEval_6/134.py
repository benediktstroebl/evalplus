from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depths = []

    parens = []

    # split by spaces
    for char in paren_string:
        if char =='':
            # a group has finished, find the max depth
            max_depth = 0
            for paren in parens:
                max_depth = max(max_depth, paren[0])
            max_depths.append(max_depth)
            # reset the parentheses list
            parens = []
        else:
            # add the paren to the parentheses list
            if char == '(':
                parens.append((1, char))
            elif char == ')':
                parens.append((0, char))
            else:
                raise ValueError(f'Character {char} is not a parenthesis.')

    return max_depths


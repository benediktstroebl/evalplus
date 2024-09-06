from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Create a list of ints for the output and a string for the input.
    levels = []
    paren_string = paren_string.strip()
    if paren_string == '':
        return levels

    # Find the level of nesting for each section and append to the output list.
    for paren in paren_string.split():
        levels.append(len(paren)-1)

    return levels


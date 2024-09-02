from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = []
    nested_parentheses = paren_string.split()

    # Iterate over the nested parentheses and update the level of nesting for each of the parentheses
    for nested_paren in nested_parentheses:
        nest_level = 0
        for i, char in enumerate(nested_paren):
            if char == '(':
                nest_level += 1
            elif char == ')':
                nest_level -= 1
        levels.append(nest_level)

    return levels


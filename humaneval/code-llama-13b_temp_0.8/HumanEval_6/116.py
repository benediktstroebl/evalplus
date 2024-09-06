from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    deepest_nesting_levels = []
    for paren_group in paren_string.split():
        if not paren_group or paren_group[0] != '(' or paren_group[-1] != ')':
            raise ValueError(f'Paren group must start and end with a paren: {paren_group}')
        paren_stack = 0
        max_paren_stack = 0
        for paren in paren_group:
            if paren == '(':
                paren_stack += 1
            elif paren == ')':
                paren_stack -= 1
            if paren_stack > max_paren_stack:
                max_paren_stack = paren_stack
            if paren_stack < 0:
                raise ValueError(f'Paren group is not balanced: {paren_group}')
        deepest_nesting_levels.append(max_paren_stack)
    return deepest_nesting_levels


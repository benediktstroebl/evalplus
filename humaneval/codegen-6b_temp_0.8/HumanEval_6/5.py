from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    all_nesting_level = []
    remaining_paren = paren_string
    balance_remaining_paren = True
    while balance_remaining_paren:
        max_nesting, remaining_paren = max_nesting_in_nested_parens(remaining_paren)
        all_nesting_level.append(max_nesting)
        if balance_remaining_paren and remaining_paren[0] == ')':
            balance_remaining_paren = False
    return all_nesting_level


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # 1. Init variables
    balance = 0
    max_level = 0
    max_level_counter = 0
    result = []

    # 2. Traverse the string
    for paren in paren_string:
        if paren == '(':
            balance += 1
        elif paren == ')':
            balance -= 1
        if balance > max_level:
            max_level = balance
            max_level_counter += 1
        if balance == 0:
            max_level_counter = 0
        if max_level_counter == max_level:
            result.append(balance)

    return result


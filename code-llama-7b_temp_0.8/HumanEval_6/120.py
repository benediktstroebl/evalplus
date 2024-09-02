from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = 0
    current_nesting = 0
    list_of_nesting = []
    for i in paren_string:
        if i == '(':
            current_nesting += 1
        if i == ')':
            current_nesting -= 1
        if current_nesting > max_nesting:
            max_nesting = current_nesting
        if i == ' ' and max_nesting == current_nesting:
            list_of_nesting.append(current_nesting)
            max_nesting = 0
    return list_of_nesting


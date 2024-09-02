from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # init list of counts to return
    return_list: List[int] = []
    # init level counter
    level: int = 0
    # iterate over string
    for char in paren_string:
        # update level counter
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1
        # update list of counts if it is the last char
        if char == ' ':
            return_list.append(level)
    return return_list


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens_nesting = []
    curr_paren_level = 0
    paren_string_list = paren_string.split(' ')
    for paren in paren_string_list:
        if paren == '(':
            curr_paren_level += 1
            parens_nesting.append(curr_paren_level)
        else:
            if len(parens_nesting) == 0:
                parens_nesting.append(0)
            curr_paren_level -= 1
            parens_nesting.pop()
    return parens_nesting

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = list(paren_string.split(' '))
    max_paren_depth = 0
    for element in paren_list:
        if element == '':
            continue
        elif '(' in element:
            paren_depth = element.count('(')
            if paren_depth > max_paren_depth:
                max_paren_depth = paren_depth
        else:  # it is a number
            continue
    return [max_paren_depth] * len(paren_list)
    # return [1] * len(paren_list)  # TODO: Implement this function.


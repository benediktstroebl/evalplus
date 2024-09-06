from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split(' ')

    deepest_depth = []
    for each_paren in paren_list:
        paren_depth = 0
        for index in range(len(each_paren)):
            if each_paren[index] == '(':
                paren_depth += 1
            if each_paren[index] == ')':
                paren_depth -= 1
            if paren_depth == 0:
                deepest_depth.append(index)
    return deepest_depth

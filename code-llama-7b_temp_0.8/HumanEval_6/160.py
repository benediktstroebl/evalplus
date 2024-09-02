from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    list_paren = paren_string.split()
    list_paren_nest = []
    for paren in list_paren:
        count = 0
        for i in range(len(paren)):
            if paren[i] == '(':
                count += 1
            if paren[i] == ')':
                count -= 1
        list_paren_nest.append(count)
    return list_paren_nest


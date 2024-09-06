from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    s_stack = []
    count = 0
    for i in range(len(paren_string)):
        if paren_string[i] =='':
            continue
        elif paren_string[i] == '(':
            s_stack.append(count)
            count = 0
        else:
            count += 1

    return s_

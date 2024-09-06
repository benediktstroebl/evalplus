from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    nest_level = 0
    for i in range(len(paren_string)):
        paren = paren_string[i]
        if paren == '(':
            nest_level += 1
            paren_stack.append(nest_level)
        elif paren == ')':
            nest_level -= 1
            if nest_level == 0:
                return paren_stack[::-1]
            else:
                paren_stack.append(nest_level)
    return []


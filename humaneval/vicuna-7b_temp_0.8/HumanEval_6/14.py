from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = 0
    nested_list = []
    for char in paren_string:
        if char == '(':
            max_nesting += 1
            nested_list.append(max_nesting)
        elif char == ')':
            max_nesting -= 1
            if max_nesting < 0:
                print("Internal error. max_nesting is", max_nesting)
            nested_list[-1] = nested_list[-1] + 1
    return nested_list


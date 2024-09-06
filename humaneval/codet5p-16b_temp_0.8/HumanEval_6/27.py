from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []
    curr_depth = 0
    max_depth = 0
    for char in paren_string:
        if char == '(':
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
        elif char == ')':
            if curr_depth == 0:
                break
            else:
                curr_depth -= 1

    result.append(max_depth)
    return result

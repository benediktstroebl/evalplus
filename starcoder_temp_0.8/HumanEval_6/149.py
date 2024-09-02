from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []
    result = []
    curr_max_nesting = 0
    curr_depth = 0
    for char in paren_string:
        if char == '(':
            curr_depth += 1
            curr_max_nesting = max(curr_max_nesting, curr_depth)
        if char == ')':
            curr_depth -= 1
        if curr_depth < 0:
            raise ValueError('There is a closing parenthesis without an opening one')
    result.append(curr_max_nesting)
    result.extend(parse_nested_parens(paren_string[curr_max_nesting + 1:]))
    return result

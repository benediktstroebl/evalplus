from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    groups = paren_string.split()
    result = []
    for group in groups:
        curr_max_depth = 0
        for paren in group:
            if paren == '(':
                curr_max_depth += 1
            elif paren == ')':
                curr_max_depth -= 1
            else:
                raise ValueError(f'Invalid character: {paren}')
            if curr_max_depth < 0:
                raise ValueError(f'Invalid character: {paren}')
        result.append(curr_max_depth)
    return result
    

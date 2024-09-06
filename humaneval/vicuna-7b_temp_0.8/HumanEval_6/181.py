from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for inner_paren in paren_string.replace(')', '').replace('(', '').split():
        # If it's a single opening paren, add 1 to the result
        if inner_paren == '(':
            result.append(1)
        # If it's a single closing paren, add 1 to the result
        elif inner_paren == ')':
            result.append(1)
        # If it's a nested paren, add the maximum of the two levels of nesting
        else:
            result.extend([max(x, y) for x, y in zip(result, inner_paren.split(','))])
    return result


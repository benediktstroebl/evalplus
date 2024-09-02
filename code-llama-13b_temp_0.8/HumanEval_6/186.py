from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        if not group:
            continue
        curr_min = 0
        curr_max = 0
        for character in group:
            if character == '(':
                curr_min += 1
                curr_max += 1
            elif character == ')':
                curr_min = min(curr_min, curr_max)
                curr_max -= 1
        result.append(curr_min)
    return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for paren_group in paren_string.split():
        if not paren_group:
            continue
        current_level = 0
        max_level = 0
        for paren in paren_group:
            if paren == '(':
                current_level += 1
                max_level = max(current_level, max_level)
            elif paren == ')':
                current_level -= 1
        result.append(max_level)
    return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    if not paren_string:
        return []

    left_paren = paren_string[0]
    right_paren = paren_string[-1]
    paren_string = paren_string[1:-1]
    if not paren_string:
        return [1]
    if left_paren not in paren_string:
        return [1]

    max_depth = 0
    for index, char in enumerate(paren_string):
        if char == left_paren:
            depth = parse_nested_parens(paren_string[index + 1:])[0] + 1
            if depth > max_depth:
                max_depth = depth
        elif char == right_paren:
            depth = parse_nested_parens(paren_string[:index])[0] + 1
            if depth > max_depth:
                max_depth = depth

    return [max_depth]

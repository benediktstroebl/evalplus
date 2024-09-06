from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []
    max_count = 0
    max_char = ''
    max_index = 0
    counts = [0] * len(paren_string)
    for i, char in enumerate(paren_string):
        if char == '(':
            counts[i] += 1
        elif char == ')':
            counts[i] -= 1
    for i in range(len(paren_string)):
        if counts[i] > max_count:
            max_count = counts[i]
            max_char = paren_string[i]
            max_index = i
    if max_count == 0:
        return [0]
    return parse_nested_parens(paren_string[:max_index] + paren_string[max_index + 1:]) + [max_count]


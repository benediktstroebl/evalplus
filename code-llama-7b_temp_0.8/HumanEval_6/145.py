from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # O(n) time and space
    count = 0
    max_count = 0
    result = []
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count > 0:
            max_count = count
        if count == 0:
            result.append(max_count)
    return result


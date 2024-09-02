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

    book = {
        '(': 1,
        ')': 1,
        '[': 2,
        ']': 2,
        '}': 3,
        '{': 3
    }

    stack = [0] * len(paren_string)
    for i, paren in enumerate(paren_string):
        if paren in book:
            stack[i] = book[paren]
    return stack


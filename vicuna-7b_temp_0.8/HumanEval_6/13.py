from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = [0] * len(paren_string)
    index = 0
    while index < len(paren_string):
        count[paren_string[index] - '('] += 1
        if paren_string[index] == '(':
            index += 1
            while paren_string[index] == '(':
                index += 1
            count[paren_string[index] - '('] += 1
    return count


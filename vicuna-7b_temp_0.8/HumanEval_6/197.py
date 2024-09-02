from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths = [0] * len(paren_string)
    result = [0] * len(paren_string)
    for i in range(len(paren_string)):
        for j in range(i):
            if paren_string[i] == '(' and paren_string[j] == ')':
                depths[i] += 1
                if depths[j] > 0:
                    depths[j] -= 1
    return depths


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    n = len(paren_string)
    max_depths = [0] * n
    for i in range(n):
        if paren_string[i] == '(':
            max_depths[i] = 1
            for j in range(i + 1, n):
                if paren_string[j] == '(':
                    max_depths[j] = max_depths[j - 1] + 1
                elif paren_string[j] == ')':
                    max_depths[j] = max_depths[j - 1] - 1
        else:
            for j in range(i - 1, -1, -1):
                if paren_string[j] == ')':
                    max_depths[j] = max_depths[j + 1] - 1
    return max_depths


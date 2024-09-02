from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    start_idx = 0
    num_nested = 0
    max_nested = 0
    for idx, char in enumerate(paren_string):
        if char == '(':
            num_nested += 1
            if num_nested > max_nested:
                max_nested = num_nested
        elif char == ')':
            num_nested -= 1
    end_idx = idx + 1
    return [max_nested, end_idx]


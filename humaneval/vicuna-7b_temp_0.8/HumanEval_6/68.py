from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting = 0
    nesting_map = {
        ')': 0,
        '(': 1,
        '[': 2,
        ']': 1,
        '{': 2,
        '}': 1
    }

    for char in paren_string:
        if char == '(':
            nesting += 1
        elif char == ')':
            nesting -= 1
        elif char == '[' or char == ']':
            nesting_map[char] = nesting
        else:
            if nesting_map[char] == nesting:
                nesting = nesting_map[char]
    return nesting


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = [0]
    current_nesting = [0]
    for char in paren_string:
        if char == "(":
            current_nesting.append(current_nesting[-1] + 1)
        elif char == ")":
            current_nesting.append(current_nesting[-1] - 1)
        max_nesting.append(max(max_nesting[-1], current_nesting[-1]))
    return max_nesting[1:]


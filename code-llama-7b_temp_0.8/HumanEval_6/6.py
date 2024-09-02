from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    num_depths = []

    def check_paren(string: str):
        depth = 0
        for char in string:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
        return depth

    for string in paren_string.split():
        num_depths.append(check_paren(string))

    return num_depths


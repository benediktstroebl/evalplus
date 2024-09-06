from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _helper(remaining_string: str) -> int:
        depth = 0
        for char in remaining_string:
            if char == '(':
                depth += 1
            elif char == ')':
                if depth == 0:
                    break
                depth -= 1
            else:
                continue
        if depth != 0:
            raise ValueError('Invalid string as input')
        return depth

    return [_helper(s) for s in paren_string.split(' ')]


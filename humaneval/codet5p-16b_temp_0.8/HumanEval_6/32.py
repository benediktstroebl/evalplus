from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def recurse(paren_string: str, depth: int) -> List[int]:
        if not paren_string:
            return depth

        paren_depth = depth
        for i, char in enumerate(paren_string):
            if char == '(':
                paren_depth += 1
            elif char == ')':
                paren_depth -= 1
            if paren_depth == 0:
                return recurse(paren_string[i+1:], depth+1)

    return recurse(paren_string, 0)


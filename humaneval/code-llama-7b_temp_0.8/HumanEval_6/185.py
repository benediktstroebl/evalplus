from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def helper(string: str) -> int:
        result, level = 0, 0
        for char in string:
            if char == '(':
                level += 1
            else:
                level -= 1
            result = max(result, level)
        return result

    return [helper(i) for i in paren_string.split()]


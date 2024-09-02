from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def counter(paren_str: str) -> int:
        count = 0
        for character in paren_str:
            if character == '(':
                count += 1
            elif character == ')':
                count -= 1
        return count

    return [counter(paren_str) for paren_str in paren_string.split()]


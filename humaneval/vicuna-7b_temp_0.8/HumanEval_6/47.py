from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_nesting(paren_string: str, current_nesting: int) -> int:
        count = 0
        for char in paren_string:
            if char == '(':
                current_nesting -= 1
            elif char == ')':
                current_nesting += 1
                count += 1
        return count

    return [count_nesting(paren_string, 0) for paren_string in paren_string.split()]


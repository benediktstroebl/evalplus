from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def nesting_level(paren_string: str) -> int:
        nesting_levels = [0] * 5 # Each group of parentheses is 5 levels of nesting
        for i, char in enumerate(paren_string):
            if char == '(':
                nesting_levels[i] += 1
            elif char == ')':
                nesting_levels[i] -= 1
                if nesting_levels[i] < 0:
                    nesting_levels[i] = 0
        return nesting_levels[0]
    return [nesting_level(i) for i in paren_string.split()]

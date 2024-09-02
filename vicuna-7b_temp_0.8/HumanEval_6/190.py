from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_group(paren: str) -> int:
        count = 0
        for char in paren:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            else:
                break
        return count

    return [count_group(paren) for paren in paren_string.split()]

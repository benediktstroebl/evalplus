from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_nested(paren_group: str, nested_count: List[int] = []):
        count = 0
        for c in paren_group:
            if c == '(':
                nested_count.append(count)
            elif c == ')':
                nested_count.pop()
                count -= 1
        return count

    nested_count = [count_nested(paren_group) for paren_group in paren_string.split()]
    return nested_count

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # --------------------------------------------------------------------------
    def is_nested(sub_string: str) -> bool:
        return sub_string.count('(') != sub_string.count(')')

    # --------------------------------------------------------------------------
    def max_level(sub_string: str) -> int:
        count = 0
        for char in sub_string:
            if char == '(':
                count += 1
            else:
                count -= 1

        return count

    # --------------------------------------------------------------------------
    return [max_level(sub_string) for sub_string in paren_string.split(' ') if is_nested(sub_string)]


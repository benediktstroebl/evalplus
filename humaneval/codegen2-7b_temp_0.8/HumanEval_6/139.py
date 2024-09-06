from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    out_string = []
    nested_parens = {')': '(', ']': '[', '}': '{'}
    for paren in paren_string:
        level = 0
        for index, char in enumerate(paren_string):
            if paren == nested_parens[char]:
                level += 1
            elif char == nested_parens[paren]:
                level -= 1
                if level == 0:
                    out_string.append(level)
    return out_

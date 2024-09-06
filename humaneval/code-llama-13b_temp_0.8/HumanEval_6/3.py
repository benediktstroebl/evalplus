from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for paren in paren_string.split():
        current_level = 0
        maximum_level = 0
        for c in paren:
            if c == '(':
                current_level += 1
            else:
                current_level -= 1
            maximum_level = max(maximum_level, current_level)
        result.append(maximum_level)
    return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # **************** IMPLEMENTATION BELOW ******************
    result = []
    for string in paren_string.split(' '):
        if len(string) == 0:
            result.append(0)
            continue
        current_level = 0
        max_level = 0
        for char in string:
            if char == '(':
                current_level += 1
                if current_level > max_level:
                    max_level = current_level
            else:
                current_level -= 1
        result.append(max_level)
    return result


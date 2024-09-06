from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    output = []
    open_count = 0
    max_count = 0

    for ch in paren_string:
        if ch == '(':
            open_count += 1
            max_count = max(max_count, open_count)
        elif ch == ')':
            open_count -= 1

        if open_count == 0:
            output.append(max_count)
            max_count = 0

    return output


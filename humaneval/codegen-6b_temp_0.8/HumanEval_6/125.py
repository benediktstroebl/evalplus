from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    """ Example - ((()()))()"""

    paren_list = []
    count = 0
    for char in paren_string:
        if char == '(':
            paren_list.append(count)
            count += 1
        elif char == ')':
            count -= 1
            paren_list.append(count)

    max_level = 0
    for i in range(len(paren_list)):
        level = abs(paren_list[i] - paren_list[i - 1])
        if level > max_level:
            max_level = level

    return [max_level, max_level]


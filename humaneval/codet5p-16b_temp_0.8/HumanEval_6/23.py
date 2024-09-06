from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.split()
    max_level = 0
    level = 0
    answer = []
    for element in paren_string:
        if element == ')':
            level -= 1
        elif element == '(':
            level += 1
            if level > max_level:
                max_level = level
        answer.append(max_level)
    return answer


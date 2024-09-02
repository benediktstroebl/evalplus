from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level = 0
    highest_level = 0
    highest_level_count = 0
    result = []
    for char in paren_string:
        if char == '(':
            level += 1
            if level > highest_level:
                highest_level = level
                highest_level_count = 1
        elif char == ')':
            level -= 1
            if level < 0:
                raise ValueError(f'Unbalanced parens: {paren_string}')
            if level == 0:
                highest_level_count += 1
        if level == 0:
            result.append(highest_level_count)
            highest_level = 0
            highest_level_count = 0
    return result


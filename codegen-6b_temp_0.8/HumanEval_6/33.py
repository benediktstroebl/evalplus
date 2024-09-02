from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_count = 0
    max_index = 0
    level = 0
    for i, p in enumerate(paren_string):
        if p == '(':
            level += 1
            if level > max_count:
                max_index = i
                max_count = level
        elif p == ')':
            level -= 1

    result = [max_count]
    for i in range(max_index, len(paren_string)):
        if paren_string[i] == '(':
            level += 1
        elif paren_string[i] == ')':
            level -= 1
        if level == 0:
            result.append(i)
            break
    return result


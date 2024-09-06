from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    idx = [0]
    level_count = [1]
    depth = 0

    for idx, char in enumerate(paren_string):
        if char == '(':
            depth += 1
            level_count.append(depth)
        elif char == ')':
            depth -= 1
            level_count.append(depth)
        else:
            pass

    max_count = max(level_count)
    return [max_count] + [level_count.index(n) for n in level_count if n != max_count]


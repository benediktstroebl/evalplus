from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parse_results = []
    cur_max_level = -1
    for level in paren_string.split():
        if level:
            cur_max_level += 1
        else:
            cur_max_level -= 1
        parse_results.append(cur_max_level)
    return parse_results


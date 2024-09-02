from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    cur_level = 0
    cur_indent = 0
    result = []
    for paren in paren_string:
        if paren == '(':
            cur_level += 1
            cur_indent += 1
        elif paren == ')':
            cur_level -= 1
            cur_indent -= 1
            if cur_level < 0:
                break
        if cur_level == 0:
            result.append(cur_indent)
    return

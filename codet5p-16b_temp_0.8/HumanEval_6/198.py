from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.replace(' ', '')
    result = []
    num_open_parens = 0
    max_level = 0
    cur_level = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            num_open_parens += 1
            cur_level += 1
        elif paren_string[i] == ')':
            if num_open_parens == 1:
                result.append(cur_level)
            else:
                num_open_parens -= 1
                cur_level -= 1
            if cur_level > max_level:
                max_level = cur_level
    return result


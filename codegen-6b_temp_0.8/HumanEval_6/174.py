from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    string_length = len(paren_string)
    nested_parens = [0] * string_length

    level_start = 0
    for i in range(string_length):
        if paren_string[i] == '(':
            level_start += 1
        elif paren_string[i] == ')':
            level_start -= 1
        nested_parens[i] = level_start

    # print(nested_parens)

    curr_level = nested_parens[0]
    levels = 1
    for i in range(1, string_length):
        if curr_level == 0:
            levels += 1
            curr_level += nested_parens[i]
        elif nested_parens[i] == 0:
            curr_level += nested_parens[i]
        else:
            curr_level = max(curr_level, nested_parens[i])
    return levels


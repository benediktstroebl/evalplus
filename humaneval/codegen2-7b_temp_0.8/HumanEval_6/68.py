from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    num_parens = 0
    max_num_parens = 0
    levels = [0] * len(paren_string)

    for index, character in enumerate(paren_string):
        if character == '(':
            num_parens += 1
            levels[index] = num_parens
        else:
            num_parens -= 1
            max_num_parens = max(max_num_parens, levels[index])
    return levels[::-1]

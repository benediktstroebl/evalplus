from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # a list of the number of open parens at each character position
    num_open_parens = [0] * (len(paren_string) + 1)
    # a list of the index of the last open paren at each character position
    last_open_paren = [-1] * (len(paren_string) + 1)

    max_paren_depth = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            num_open_parens[i + 1] = num_open_parens[i] + 1
            max_paren_depth = max(max_paren_depth, num_open_parens[i + 1])
            last_open_paren[i + 1] = i
        elif char == ')':
            if last_open_paren[i + 1] == -1:
                return None
            num_open_parens[i + 1] = num_open_parens[i]
            max_paren_depth = max(max_paren_depth, num_open_parens[i])
            last_open_paren[i + 1] = last_open_paren[i]
        else:
            num_open_parens[i + 1] = num_open_parens[i]
            max_paren_depth = max(max_paren_depth, num_open_parens[i])
            last_open_paren[i + 1] = last_open_paren[i]

    return [max_paren_depth] * len(paren_string)


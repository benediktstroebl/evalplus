from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    res = []
    i = 0
    while i < len(paren_string):
        # Find the longest instance of a paren
        count = 1
        while paren_string[i] == ')':
            prev = i - count
            if paren_string[prev] == '(':
                count += 1
            i += 1
        # Find the position of the last paren
        while paren_string[i] != '(':
            i += 1
        # Get the number of parentheses
        num_parens = count
        # Get the position of the last paren
        prev = i - count
        # Get the number of left parentheses
        left_parens = prev - 1
        # Get the number of right parentheses
        right_parens = i - 1
        # Get the total depth
        depth = left_parens + num_parens + right_parens
        # Get the maximum depth seen so far
        if len(res) == 0 or depth > res[-1]:
            res.append(depth)
        i += 1
    return res


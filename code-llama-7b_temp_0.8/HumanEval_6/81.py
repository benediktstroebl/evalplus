from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # first find out the number of parentheses
    parentheses_in_str = paren_string.count('(') + paren_string.count(')')
    # then create a list of appropriate length
    max_level_nested_parens = [0] * parentheses_in_str

    for group in paren_string.split(' '):
        count = 0
        for c in group:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        # we only need to add count to the first item in the list
        max_level_nested_parens[0] = max(max_level_nested_parens[0], count)

    return max_level_nested_parens


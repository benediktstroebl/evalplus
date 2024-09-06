from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split()
    max_depth = 0
    for paren in parens:
        curr_depth = 0
        for i, char in enumerate(paren):
            if char == '(':
                curr_depth += 1
            elif char == ')':
                curr_depth -= 1
            if curr_depth < 0:
                curr_depth = 0
                break
            if curr_depth > max_depth:
                max_depth = curr_depth
        if curr_depth < 0:
            curr_depth = 0
        if max_depth < curr_depth:
            max_depth = curr_depth
    return [max_depth]


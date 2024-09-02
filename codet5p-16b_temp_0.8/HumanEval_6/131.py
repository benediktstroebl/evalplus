from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.replace(' ', '')
    max_nesting = 0
    curr_nesting = 0
    output: List[int] = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            curr_nesting += 1
            if curr_nesting > max_nesting:
                max_nesting = curr_nesting
        elif paren_string[i] == ')':
            curr_nesting -= 1
        output.append(max_nesting)
    return output


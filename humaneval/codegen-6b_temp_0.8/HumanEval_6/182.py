from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Process the string
    parentheses = paren_string.strip()
    parens = []
    open_parens = 0

    for i, ch in enumerate(parens):
        if ch == '(':
            open_parens += 1
        elif ch == ')':
            current_open_parens = len(parens) - parens[::-1].index('(') - 1
            open_parens -= 1
            if open_parens < current_open_parens:
                parens[-1] = i
                parens[current_open_parens] = -1

    # Find the max
    max_index = len(parens) - parens[::-1].index('(')
    return [max_index] + [i - 1 for i in parens[-1:0:-1]]


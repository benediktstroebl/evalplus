from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    open_brackets = 0
    for i, character in enumerate(paren_string):
        if character == '(':
            open_brackets += 1
        elif character == ')':
            open_brackets -= 1
        if open_brackets < 0:
            break
        stack.append(open_brackets)
    return stack[::-1]


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Replace all spaces in string with a few other character
    paren_string = paren_string.replace(' ', '{')

    stack = []
    nestings = []
    max_nesting = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(i)
        elif c == ')':
            nestings.append(stack.pop())
        elif c == '{':
            nestings.append(stack.pop())
            max_nesting = max(max_nesting, len(stack))
    return [max_nesting, len(nestings)]


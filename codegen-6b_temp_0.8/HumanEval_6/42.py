from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # use a stack to store indices of parens
    stack = []
    no_opening_parens = []

    # go over all characters in the string and find opening parens
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            # store the index of the most nested closing parenthesis
            nest_level = stack.pop() if stack else "out of bounds"
            no_opening_parens.append(i - nest_level)

    return no_opening_parens

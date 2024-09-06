from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    numbers = []
    current = 0
    for i, character in enumerate(paren_string):
        if character == '(':
            stack.append(character)
            current = len(stack) - 1
        elif character == ')' and stack[current] == '(':
            stack.pop()
            numbers.append(current)
            current = len(stack) - 1 if len(stack) > 0 else 0
        elif character == ')' and stack[current] != '(':
            stack.append(character)
            current = len(stack) - 1
    return numbers


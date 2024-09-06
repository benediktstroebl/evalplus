from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    index = 0
    in_parentheses = False
    is_balanced = True
    depth = 0
    nested_parens = []
    level = []

    while index < len(paren_string):

        if paren_string[index] == '(':
            depth += 1
            level.append(depth)
            in_parentheses = True
            index += 1
        elif paren_string[index] == ')':
            depth -= 1
            in_parentheses = False

            if not depth:
                nested_parens.append(level.pop())
            index += 1

    nested_parens.append(len(level))
    return nested_parens


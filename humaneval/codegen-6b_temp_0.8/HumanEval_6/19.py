from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    index = 0
    nested_parens = []
    while index < len(paren_string):
        if paren_string[index] == '(':
            level = 1
            i = index + 1
            while i < len(paren_string):
                if (paren_string[i] == '('):
                    level += 1
                elif (paren_string[i] == ')'):
                    level -= 1
                    if level == 0:
                        nested_parens.append(i - index)
                        break
                i += 1
        index += 1
    return nested_parens


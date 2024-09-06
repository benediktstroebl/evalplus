from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens = [paren_string]
    while nested_parens:
        paren_string = nested_parens.pop(0)
        paren_level = 0
        new_parens = []
        for paren in paren_string:
            if paren == '(':
                paren_level += 1
                new_parens.append(paren)
            elif paren == ')':
                paren_level -= 1
                new_parens.append(paren)
            elif paren_level == 0:
                new_parens.append(paren)
            elif paren_level > 0:
                new_parens.append(paren)
        nested_parens.append(new_parens)

    return [len(level) for level in nested_parens]


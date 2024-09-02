from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split()

    result = []

    for i in parens:
        depth = 0
        for char in i:
            if char == "(":
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                result.append(i)
                break
    return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_level = 0
    is_balanced = True
    parens = []

    for i in range(len(paren_string)):
        is_balanced, nesting_level = _is_paren_balanced(paren_string[i], nesting_level, is_balanced)

        if is_balanced and nesting_level > 1:
            parens.append(nesting_level)

    return parens


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens = [paren for paren in paren_string.split(' ')]
    maximum_nesting_levels = [0] * len(nested_parens)
    nesting_levels = [0] * len(nested_parens)

    for i, paren in enumerate(nested_parens):
        for j, sub_paren in enumerate(paren):
            if sub_paren == '(':
                nesting_levels[j] += 1
                maximum_nesting_levels[i] = max(nesting_levels[j], maximum_nesting_levels[i])
            elif sub_paren == ')':
                if nesting_levels[j] > 0:
                    nesting_levels[j] -= 1
                    maximum_nesting_levels[i] = max(nesting_levels[j], maximum_nesting_levels[i])

    return maximum_nesting_levels


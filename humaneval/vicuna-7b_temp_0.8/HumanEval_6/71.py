from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_levels = []
    current_nesting = 0
    for opening_paren, closing_paren in (
            ((0, ''), ''),
            ((0, ''), ''),
            ((1, '('), ')'),
            ((1, ')'), ''),
            ((2, '(', ')'), ''),
            ((1, ')', ''), ''),
            ((2, '(', ')'), ')'),
            ((2, '(', '(', ')'), ''),
            ((3, '(', ')'), ''),
            ((3, '(', '(', '(', ')'), ')'),
            ((3, '(', '(', '(', '(', ')'), ')'),
            ):
        nesting_levels.append(current_nesting)
        current_nesting = nesting_levels[-1]
        closing_paren = next((c for o, c in opening_paren), None)
        if closing_paren is None:
            nesting_levels.pop()
            current_nesting -= 1
            continue
        opening_paren = next((o for o, c in closing_paren), None)
        if opening_paren is None:
            nesting_levels.pop()
            current_nesting -= 1
            continue
        if current_nesting == 0:
            current_nesting = nesting_levels[-1]
            nesting_levels.pop()
    return nesting_levels


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens_count = 0
    last_opened_paren_idx = -1
    nested_paren_level = 0
    for idx, char in enumerate(paren_string):
        if char == '(':
            parens_count += 1
        elif char == ')':
            parens_count -= 1
            if parens_count == 0:
                nested_paren_level = max(nested_paren_level, parens_count)
        last_opened_paren_idx = idx

    return [nested_paren_

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens_count = {}
    current_nesting = 0
    for opening_paren in paren_string:
        for closing_paren in paren_string:
            if opening_paren == closing_paren:
                nested_parens_count[current_nesting] = 0
                current_nesting += 1
            else:
                for i in range(opening_paren, closing_paren):
                    nested_parens_count[current_nesting] += 1
                current_nesting = opening_paren
    return nested_parens_count.values()
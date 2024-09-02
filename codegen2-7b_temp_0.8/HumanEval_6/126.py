from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []

    for paren in paren_string.split():
        open_paren_count = paren.count('(')
        if open_paren_count % 2!= 0:
            raise Exception(f"Expected an even number of open parenthesis but got {open_paren_count}")

        nested_paren_count = open_paren_count // 2
        nested_parens.append(nested_paren_count)

    return nested_parens

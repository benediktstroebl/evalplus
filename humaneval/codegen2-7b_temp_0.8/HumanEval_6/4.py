from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []

    def parse_nested_parens_helper(paren_string: str, nested_parens: List[int]) -> None:
        nonlocal nested_parens
        if not paren_string:
            return
        if paren_string[0] == '(' and paren_string[-1] == ')':
            nested_parens.append(len(paren_string))
            return
        parse_nested_parens_helper(paren_string[1:], nested_parens)

    parse_nested_parens_helper(paren_string, nested_parens)
    

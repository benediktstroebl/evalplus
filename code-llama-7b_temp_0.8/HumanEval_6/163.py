from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [
        max(
            nested_parentheses.count("(")
            - nested_parentheses.count(")")
            for nested_parentheses in nested_parens_list
        )
        for nested_parens_list in [
            nested_paren_str.split(" ") for nested_paren_str in paren_string.split(" ")
        ]
    ]


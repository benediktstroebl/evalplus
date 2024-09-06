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
            0,
            sum(
                1
                if char == ")" and stack[-1] == "("
                else -1
                if char == "("
                else 0
                for char in paren_string
            ),
        )
        for paren_string in paren_string.split(" ")
    ]


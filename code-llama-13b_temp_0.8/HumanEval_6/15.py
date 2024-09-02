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
            len(match.group(0)) - len(match.group(1))
            for match in re.finditer(r'(\(([^()]*|(?2))*\))', group)
        )
        for group in paren_string.split()
    ]


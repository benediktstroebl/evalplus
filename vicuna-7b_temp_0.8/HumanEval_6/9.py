from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for match in re.finditer(r'\((.+?)\)', paren_string):
        depth = 1
        for opening_paren in match.group(0).strip().split():
            i = paren_string.find(opening_paren)
            j = paren_string.find(opening_paren, i + 1)
            depth = max(depth, j - i - 1)
        result.append(depth)
    return result


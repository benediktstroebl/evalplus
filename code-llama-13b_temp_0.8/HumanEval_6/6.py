from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [max(map(lambda x: x[0] - x[1], zip(count, count[1:][paren_string[start:end].count('('):])))
            for start, end, count in zip(range(0, len(paren_string), 2), range(2, len(paren_string), 2),
                                         range(1, len(paren_string) + 1))]


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = {}

    for s in paren_string:
        if s:
            for i in range(1, len(s)):
                if count.get(s[:i]):
                    count[s[:i]] = count[s[:i]] + 1
                else:
                    count[s[:i]] = 1
            if count.get(s):
                count[s] = count[s] + 1
            else:
                count[s] = 1

    return list(count.keys())


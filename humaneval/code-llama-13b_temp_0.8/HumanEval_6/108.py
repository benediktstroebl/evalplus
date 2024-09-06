from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_deep = 0
    res = []
    for s in paren_string.split():
        deep = 0
        for c in s:
            if c == '(':
                deep += 1
                max_deep = max(deep, max_deep)
            else:
                deep -= 1
        res.append(max_deep)
        max_deep = 0
    return res


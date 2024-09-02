from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 1
    result = []
    for s in paren_string.split(' '):
        if s[0] == '(':
            level = 1
            for i in range(1, len(s)):
                if s[i] == '(':
                    level += 1
                elif s[i] == ')':
                    level -= 1
                if level == 0:
                    result.append(i)
                    level = 1
            max_level = max(max_level, level)
    return result


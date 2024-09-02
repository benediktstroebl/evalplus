from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Find the first unmatched close parenthesis (lpad is the index of the first unmatched close parenthesis)
    lpad = len(paren_string)
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            lpad = i
            break
    # Find the first unmatched open parenthesis (rpad is the index of the first unmatched open parenthesis)
    rpad = len(paren_string)
    for i in range(len(paren_string) - 1, -1, -1):
        if paren_string[i] == ')':
            rpad = i
            break

    # Each group has the same depth since all groups are balanced
    depth = lpad - rpad

    # Check for nested groups
    for i in range(lpad, rpad):
        if paren_string[i] == '(':
            el = i
            while el < rpad:
                el += 1
                if paren_string[el] == '(':
                    depth += 1
                elif paren_string[el] == ')':
                    depth -= 1
                    if depth == 0:
                        break
    return [depth, lpad, rpad]


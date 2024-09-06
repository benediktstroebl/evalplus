from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_counts = [0]
    highest = 0
    for i in range(1, len(paren_string)):
        if paren_string[i] == '(':
            paren_counts.append(0)
            highest = max(highest, paren_counts[-1])
        elif paren_string[i] == ')':
            paren_counts[-2] += 1
            highest = max(highest, paren_counts[-2])
        else:
            pass
    return paren_counts


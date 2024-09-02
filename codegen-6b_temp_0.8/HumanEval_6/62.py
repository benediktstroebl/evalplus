from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level_paren_counts = []
    stack = []
    for i, paren in enumerate(paren_string):
        if paren == '(':
            stack.append(i)
        elif paren == ')':
            count = 0
            for j in stack[::-1]:
                if j < i:
                    break
                count += 1
            level_paren_counts.append(count)
            stack.pop()

    return level_paren_counts


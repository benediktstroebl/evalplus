from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = [0]
    for open_paren, close_paren in ((open_paren, close_paren) for open_paren, close_paren in (
        (('(', ')'), '(', ')'), (')', '(', ')'), (')', '(', ')'), (')', '(', ')')) if paren_string.count(open_paren) == paren_string.count(close_paren)]:
        level = 0
        open_paren_idx = paren_string.index(open_paren)
        close_paren_idx = paren_string.index(close_paren, open_paren_idx) + 1
        for i in range(open_paren_idx, close_paren_idx):
            levels[-1] += 1
            if paren_string[i] == '(':
                level += 1
            elif paren_string[i] == ')':
                level -= 1
                if level == 0:
                    break
        if level > 0:
            levels.append(level)
    return levels


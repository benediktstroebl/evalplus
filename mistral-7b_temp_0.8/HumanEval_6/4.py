from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []
    paren_list = []
    for paren_group in paren_string.split():
        if len(paren_group) == 0:
            continue
        depth = 0
        for i, paren in enumerate(paren_group):
            if paren == '(':
                depth += 1
            elif paren == ')':
                depth -= 1
            else:
                raise ValueError(f'Unexpected character {paren}')
            if depth < 0:
                raise ValueError(f'Negative depth {depth} for {paren_group}')
            if depth > 0:
                paren_list.append(depth)
    return paren_list

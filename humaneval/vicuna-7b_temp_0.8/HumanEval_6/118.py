from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested = []
    for opening, closing in zip(paren_string.split(','), reversed(paren_string.split(','))):
        if not opening:
            continue
        depth = 0
        for i in range(len(opening)):
            if opening[i] == closing[i]:
                depth += 1
                if not closing[i + 1]:
                    closing = closing[:i]
                    depth -= 1
        nested.append(depth)
    return nested


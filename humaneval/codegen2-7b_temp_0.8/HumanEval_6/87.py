from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nest_counts = [0]
    for i, paren in enumerate(paren_string.replace(" ", "")):
        if paren == "(":
            nest_counts.append(1)
        elif paren == ")":
            nest_counts[-1] -= 1
            if nest_counts[-1] == 0:
                nest_counts.pop()
    return nest_counts[::-1

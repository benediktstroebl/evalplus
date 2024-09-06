from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    paren_level = 0
    for i, ch in enumerate(paren_string):
        if ch == "(":
            paren_level += 1
        elif ch == ")":
            paren_level -= 1
            if paren_level < 0:
                raise ValueError(
                    f"Unmatched parenthesis at {i}:\n {paren_string}"
                )
        if paren_level == 0:
            stack.append(i)
    return

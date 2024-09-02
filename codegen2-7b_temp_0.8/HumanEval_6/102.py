from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_count = 0
    paren_stack = []
    for char in paren_string:
        if char == "(":
            paren_count += 1
            paren_stack.append(char)
        elif char == ")":
            paren_count -= 1
            if paren_count < 0:
                raise ValueError(
                    f"Expected number of nested parentheses, got {paren_count} instead.")
            paren_stack.pop()

    return [len(paren_stack)] + paren_stack[::-

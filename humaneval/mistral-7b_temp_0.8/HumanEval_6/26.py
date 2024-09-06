from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    output = []
    for paren_group in paren_string.split():
        cur_output = 0
        for c in paren_group:
            if c == "(":
                cur_output += 1
            elif c == ")":
                cur_output -= 1
            if cur_output < 0:
                raise ValueError("Illegal sequence of parentheses.")
        output.append(cur_output)
    return output


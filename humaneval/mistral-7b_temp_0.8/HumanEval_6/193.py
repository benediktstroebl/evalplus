from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # TODO: Think of more elegant solutions
    output = []
    # Every time we enter a new pair of parentheses, increase the value by 1
    # Every time we exit a pair of parentheses, decrease the value by 1
    cur_level = 0
    for c in paren_string:
        if c == "(":
            cur_level += 1
        elif c == ")":
            cur_level -= 1
        output.append(cur_level)

    return output

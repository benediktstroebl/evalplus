from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    _paren_level = 0
    _paren_stack = []

    for _ in range(len(paren_string)):
        if paren_string[_] == "(":
            _paren_level += 1
            _paren_stack.append(_paren_level)
        elif paren_string[_] == ")":
            _paren_level -= 1
    return _paren_stack


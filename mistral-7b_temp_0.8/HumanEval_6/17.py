from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    bracket_values = list(bracket_map.values())
    bracket_keys = list(bracket_map.keys())
    bracket_map_inv = {v: k for k, v in bracket_map.items()}
    bracket_keys_inv = [bracket_map_inv[v] for v in bracket_values]
    stack: List[str] = []
    nested_parens: List[int] = []
    for paren in paren_string:
        if paren in bracket_keys:
            stack.append(paren)
        elif paren in bracket_keys_inv:
            stack.pop()
        else:
            continue
        if len(stack) > nested_parens[-1]:
            nested_parens.append(len(stack))
    return nested_parens


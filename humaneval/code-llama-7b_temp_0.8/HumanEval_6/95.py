from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = [1]
    current_level = 0

    for ch in paren_string:
        if ch == '(':
            current_level += 1
            max_level.append(current_level)
        elif ch == ')':
            if current_level > 0:
                current_level -= 1
        else:
            raise Exception(f"invalid character {ch}")

    return max_level[1:]


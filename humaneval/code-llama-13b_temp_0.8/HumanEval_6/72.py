from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # [('(', 1), ('(', 2), (')', 2), ('(', 2), (')', 2), ('(', 3), (')', 3), ('(', 3), (')', 3), ('(', 3), (')', 3), ('(', 3), (')', 3), ('(', 3), ('(', 4), (')', 4), (')', 2), ('(', 2), ('(', 3), ('(', 4), (')', 4), (')', 3), (')', 2), ('(', 1), (')', 1)]

    max_depth = 0
    counter = 0
    depth = []
    for char in paren_string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            if counter < 0:
                raise ValueError(f'Unexpected ")" at position {depth}')
        depth.append(counter)

    max_depth = max(depth)
    return [depth.count(max_depth)]


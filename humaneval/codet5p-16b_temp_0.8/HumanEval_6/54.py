from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parsed_nested_parens = []
    nested_paren_count = 0
    current_nested_paren_depth = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            current_nested_paren_depth += 1
            nested_paren_count += 1
        elif char == ')':
            current_nested_paren_depth -= 1
            if current_nested_paren_depth < 0:
                current_nested_paren_depth = 0
                parsed_nested_parens.append(current_nested_paren_depth)
                current_nested_paren_depth = 0
        if nested_paren_count == 0:
            parsed_nested_parens.append(current_nested_paren_depth)
            current_nested_paren_depth = 0
            nested_paren_count = 0
    return parsed_nested_parens


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    deepest_nest_levels = []

    for group in paren_string.split():
        left_paren_count, right_paren_count = 0, 0

        for i, char in enumerate(group):
            if char == '(':
                left_paren_count += 1
            elif char == ')':
                right_paren_count += 1

            if right_paren_count > left_paren_count:
                break

        deepest_nest_levels.append(left_paren_count + right_paren_count)

    return deepest_nest_levels


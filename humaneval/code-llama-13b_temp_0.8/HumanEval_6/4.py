from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    deepest_nesting = []

    for group in paren_string.split():
        # if the group is invalid, return -1
        if not group.startswith('(') or not group.endswith(')'):
            deepest_nesting.append(-1)
            continue

        current_nesting = 0
        deepest_level = 0
        for paren in group:
            if paren == '(':
                current_nesting += 1
                if current_nesting > deepest_level:
                    deepest_level = current_nesting
            elif paren == ')':
                current_nesting -= 1

        deepest_nesting.append(deepest_level)

    return deepest_nesting


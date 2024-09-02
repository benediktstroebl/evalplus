from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # pylint: disable=no-else-return,no-else-break

    if not paren_string:
        return []

    output = []

    for group in paren_string.split():
        if group == '()':
            output.append(1)
            continue

        if group[0] == '(' and group[-1] == ')':
            if group[1:-1]:
                output.append(2 + parse_nested_parens(group[1:-1]))
            else:
                output.append(1)
        else:
            break

    return output


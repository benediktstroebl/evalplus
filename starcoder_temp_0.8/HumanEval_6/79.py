from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []

    # Base case
    if len(paren_string) == 0:
        return result

    if paren_string[0] == ')':
        return result

    if paren_string[-1] == '(':
        return result

    # Recursive cases
    left_count = 0
    right_count = 0
    for index in range(len(paren_string)):
        if paren_string[index] == '(':
            left_count += 1
        elif paren_string[index] == ')':
            right_count += 1
        if left_count == right_count:
            result.append(right_count)
            return result
        elif left_count > right_count:
            result.append(left_count)
            return result
        elif right_count > left_count:
            result.append(right_count)
            return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Base case
    if len(paren_string) == 0:
        return []

    result = []

    open_counter = 0
    for char in paren_string:
        if char == '(':
            open_counter += 1
        elif char == ')':
            if open_counter == 0:
                raise ValueError('Mismatched parentheses')
            open_counter -= 1
            if open_counter == 0:
                result.append(0)

    if open_counter != 0:
        raise ValueError('Mismatched parentheses')

    if len(result) == 0:
        return []
    else:
        max_level = max(result)
        result = [res + 1 if res != max_level else res for res in result]
        return result


from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Parse string into [char1, char2, char3, ..., charN]
    paren_string = list(paren_string)
    result = []
    max = 0
    while len(paren_string) != 0:
        if paren_string[0] == '(':
            result.append(1)
            paren_string = paren_string[1:]
        elif paren_string[0] == ')':
            if result[-1] > max:
                max = result[-1]
            result = result[:-1]
            paren_string = paren_string[1:]
        else:
            raise ValueError("Invalid input. Expected input to be a string expecting characters in parens")
    return result


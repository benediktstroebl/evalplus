from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # The idea is to parse the string character by character
    # and maintain a counter for the number of open parentheses
    # as well as the deepest level of nesting we have seen so far
    counter, deepest_level = 0, 0
    output = []
    for character in paren_string:
        if character == '(':
            counter += 1
            deepest_level = max(deepest_level, counter)
        elif character == ')':
            counter -= 1
        if counter == 0:
            output.append(deepest_level)
            deepest_level = 0
    return output


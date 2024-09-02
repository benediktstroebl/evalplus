from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    deepest_level = 0
    result = []
    for i in range(len(paren_string)):
        curr_char = paren_string[i]
        if curr_char == '(':
            if i == 0 or paren_string[i - 1] == ')':
                deepest_level += 1
        elif curr_char == ')':
            if i == 0 or paren_string[i - 1] == '(':
                deepest_level -= 1
        result.append(deepest_level)
    return result


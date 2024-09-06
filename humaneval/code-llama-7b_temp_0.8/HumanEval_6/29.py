from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # base cases
    if not paren_string:
        return []

    if '(' not in paren_string and ')' not in paren_string:
        return [1]

    # recursive cases
    l_nest_counter = 0
    r_nest_counter = 0
    max_level = 0
    level = 0
    output = []
    i = 0
    while i < len(paren_string):
        char = paren_string[i]
        if char == '(':
            l_nest_counter += 1
        elif char == ')':
            r_nest_counter += 1
        if l_nest_counter == r_nest_counter:
            level = max(level, max_level)
            output.append(level)
            max_level = 0
        elif l_nest_counter > r_nest_counter:
            max_level += 1
        elif l_nest_counter < r_nest_counter:
            max_level -= 1
        i += 1

    return output


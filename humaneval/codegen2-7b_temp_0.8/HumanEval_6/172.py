from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parsed_nested_parens = []
    for paren_string in paren_string.split():
        current_level = 0
        for i, _ in enumerate(paren_string):
            if paren_string[i] == '(':
                current_level += 1
            elif paren_string[i] == ')':
                current_level -= 1
                if current_level == -1:
                    break
        parsed_nested_parens.append(current_level)
    return parsed_nested_paren

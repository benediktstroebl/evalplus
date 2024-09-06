from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    max_level = -1

    for paren_char in paren_string:
        if paren_char == ')':
            current_level = len(stack)
            if current_level > max_level:
                max_level = current_level
            stack.pop()
        else:
            stack.append(paren_char)

    return [max_level + 1] + [len(stack)] * (max_level + 1)


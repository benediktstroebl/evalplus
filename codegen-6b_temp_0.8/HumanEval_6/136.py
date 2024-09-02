from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []

    parenstack = []
    max_level = 0
    paren_string = paren_string.strip()
    char_index = -1
    while char_index < len(paren_string)-1:
        char = paren_string[char_index]
        if char == '(':
            parenstack.append('(')
        else:
            if len(parenstack) == 0:
                break
            level = 1
            while parenstack:
                top_level = parenstack.pop()
                if top_level == '(':
                    level += 1
                else:
                    level -= 1
                    if level == 0:
                        break
            if level > max_level:
                max_level = level

        char_index += 1

    if len(parenstack) == 0:
        return [max_level]

    return []


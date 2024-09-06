from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    outside_braces = []
    inside_braces = []
    paren_groups = []
    i = 0
    length = len(paren_string)
    while i < length:
        char = paren_string[i]
        if char == ')' and not inside_braces:
            paren_groups.append(''.join(outside_braces))
            outside_braces = []
        elif char == '(':
            if not inside_braces:
                inside_braces.append(char)
            else:
                inside_braces.append(char)
        elif char == ')':
            if inside_braces:
                inside_braces.pop()
            else:
                outside_braces.append(char)
        else:
            outside_braces.append(char)
        i += 1
    if inside_braces:
        paren_groups.append(''.join(outside_braces))
    else:
        paren_groups.append(''.join(outside_braces[:-1]))
    return paren_groups


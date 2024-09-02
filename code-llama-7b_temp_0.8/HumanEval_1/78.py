from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    current_group = ''
    level = 0
    for c in paren_string:
        if c == '(':
            level += 1
            current_group += '('
        elif c == ')':
            level -= 1
            if level < 0:
                raise ValueError
            else:
                current_group += ')'
                if level == 0:
                    groups.append(current_group)
                    current_group = ''
    if level > 0:
        raise ValueError
    return groups


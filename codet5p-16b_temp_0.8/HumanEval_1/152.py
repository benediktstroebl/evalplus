from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(' ', '')
    open_parens = []
    current_group = []
    for char in paren_string:
        if char == '(':
            open_parens.append(char)
            current_group.append(char)
        elif char == ')':
            open_parens.pop()
            current_group.append(char)
            if len(open_parens) == 0:
                if current_group[0] == '(':
                    current_group.pop(0)
                    current_group.append('()')
                else:
                    current_group.pop(0)
                    current_group.append('()')
        else:
            current_group.append(char)
    return current_group


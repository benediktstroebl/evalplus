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
    paren_string_list = list(paren_string)
    paren_group = []
    result = []
    for paren in paren_string_list:
        if paren == '(':
            paren_group.append(paren)
        elif paren == ')':
            if paren_group:
                paren_group.pop()
            else:
                paren_group.append(paren)
        if not paren_group:
            result.append(''.join(paren_group))
            paren_group = []
    return result


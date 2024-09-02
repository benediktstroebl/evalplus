from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    if len(paren_string) == 1 and paren_string[0] != '(' and paren_string[0] != ')':
        return []
    paren_string = paren_string.replace(' ', '')
    first_paren = paren_string.find('(')
    last_paren = paren_string.rfind(')')
    if first_paren == -1 or last_paren == -1:
        return []
    if first_paren != last_paren:
        return [paren_string[first_paren:last_paren+1]]
    return separate_paren_groups(paren_string[:first_paren]) + [paren_string[first_paren:last_paren+1]] + separate_paren_groups(paren_string[last_paren+1:])


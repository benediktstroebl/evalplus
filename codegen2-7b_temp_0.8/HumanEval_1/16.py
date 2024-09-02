from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    p_string = paren_string.replace(' ','')
    paren_count = 0
    paren_list = []
    for p_char in p_string:
        if p_char == '(':
            paren_count += 1
            paren_list.append(p_char)
        elif p_char == ')':
            paren_count -= 1
            paren_list.append(p_char)
    return paren_list

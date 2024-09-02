from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    start_pos = 0
    length = len(paren_string)
    while start_pos < length:
        if paren_string[start_pos] == '(':
            paren_list.append(paren_string[start_pos:])
            paren_string = paren_string[:start_pos] + paren_string[start_pos + 1:]
        else:
            start_pos += 1
    paren_list.append(paren_string)
    for i in range(len(paren_list)):
        paren_list[i] = str(paren_list[i]).replace(' ', '')
    return paren_list


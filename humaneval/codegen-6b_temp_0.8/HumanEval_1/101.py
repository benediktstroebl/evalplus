from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    string_list = ['']
    separated_group = False
    for char in paren_string:
        if char == ')':
            if string_list[-1] == '(':
                string_list.pop()
            else:
                separated_group = False
        elif char == '(':
            string_list.append('')
            separated_group = True
        elif char == ' ':
            pass
        else:
            string_list[-1] += char
            separated_group = True
    if not separated_group:
        return [paren_string]
    return string_list


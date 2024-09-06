from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    pass
    parens_list = []
    open_paren_list = []
    temp_paren_list = []
    open_paren_list.append(paren_string[0])
    for i, char in enumerate(paren_string):
        if i!= 0:
            temp_paren_list.append(char)
            if char == '(':
                open_paren_list.append(char)
            elif char == ')':
                open_paren_list.pop()
        if not open_paren_list:
            parens_list.append(''.join(temp_paren_list))
            temp_paren_list = []
    return parens_list


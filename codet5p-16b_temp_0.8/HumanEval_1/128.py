from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_groups = []
    start_index = 0
    curr_paren_group = ''
    for index in range(len(paren_string)):
        curr_char = paren_string[index]
        if curr_char == '(' or curr_char == ')' or curr_char =='':
            if curr_paren_group == '':
                start_index = index
            else:
                curr_paren_group += curr_char
            continue
        curr_paren_group += curr_char
        if curr_paren_group == ')':
            curr_paren_group = '('
        elif curr_paren_group == '(':
            curr_paren_group = ')'
        if curr_paren_group == ')' and paren_string[index-1] == ')':
            curr_paren_group = ''
        if curr_paren_group == '(':
            if paren_string[index+1] == ')':
                curr_paren_group = ''
            else:

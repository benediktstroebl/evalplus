from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    str_list = []
    cur_str = ""
    for paren in paren_string:
        if paren == '(':
            paren_stack.append(paren)
        elif paren == ')':
            if len(paren_stack) == 0:
                raise ValueError('Imbalanced paren string')
            if len(paren_stack) == 1:
                str_list.append(cur_str)
                cur_str = ''
                paren_stack.pop()
            else:
                paren_stack.pop()
        else:
            cur_str += paren
    return str_list


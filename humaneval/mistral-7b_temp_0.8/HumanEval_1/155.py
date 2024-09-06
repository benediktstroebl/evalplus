from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # TODO: Implement this method
    # Raise NotImplementedError
    if paren_string == '':
        return []
    else:
        paren_list = []
        flag = True
        paren_string = paren_string.strip()
        for paren in paren_string:
            if flag and paren == '(':
                paren_list.append('(')
            elif flag and paren == ')':
                paren_list.append(')')
                flag = False
            elif flag == False:
                paren_list.append(paren)
                flag = False
            else:
                paren_list.append(paren)
        if flag == True:
            paren_list.append('')
        paren_list.append('')
        return paren_list


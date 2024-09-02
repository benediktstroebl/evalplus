from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    return_list = []
    paren_list = [paren_string]
    while paren_list:
        paren_group = paren_list.pop()
        index = paren_group.find('(')
        while index!= -1:
            new_group = paren_group[index + 1:]
            paren_group = paren_group[:index]
            paren_list.append(paren_group)
            paren_list.append(new_group)
            index = new_group.find('(')
        return_list.append(paren_group)
    return return_list


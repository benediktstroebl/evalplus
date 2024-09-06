from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_paren = list(paren_string)

    out_list = []
    temp_string = []
    for letter in list_paren:
        if letter == '(':
            temp_string.append(letter)
        elif letter == ')':
            temp_string.append(letter)

            if len(temp_string) == 1:
                out_list.append(temp_string[0])
            elif len(temp_string) > 1:
                out_list.append(''.join(temp_string))
            temp_string = []

    return out_list


from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_idx = 0
    output_list = []
    for idx in range(len(paren_string)):
        if paren_string[idx] == '(':
            if idx != 0 and paren_string[idx - 1] != ' ':
                raise ValueError('Input string is not balanced')
        elif paren_string[idx] == ')':
            if idx == 0:
                raise ValueError('Input string is not balanced')
            if paren_string[idx - 1] == ' ' or idx == len(paren_string) - 1:
                output_list.append(paren_string[start_idx:idx + 1])
                start_idx = idx + 1
    return output_list


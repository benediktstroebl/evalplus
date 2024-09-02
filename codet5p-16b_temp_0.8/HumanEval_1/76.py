from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []

    curr_list = []
    open_paren = 0
    closed_paren = 0

    for paren in paren_string:
        if paren == '(':
            open_paren += 1
            curr_list.append(paren)
        elif paren == ')':
            closed_paren += 1
            curr_list.append(paren)
            if open_paren == closed_paren:
                result.append(''.join(curr_list))
                curr_list = []
                open_paren = closed_paren = 0
            else:
                curr_list = []

    return result


from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_index = 0
    end_index = 0
    found_open = False
    lst = []
    for index, char in enumerate(paren_string):
        if char == '(':
            found_open = True
            start_index = index
        elif char == ')':
            if found_open:
                end_index = index + 1
                lst.append(paren_string[start_index:end_index])
                found_open = False
            else:
                return lst
    return lst

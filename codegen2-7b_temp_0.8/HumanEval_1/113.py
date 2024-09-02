from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    lst = []

    string = paren_string.strip()

    i = 0
    while i < len(string):
        if string[i] == '(':
            j = string.find(')', i)
            if j > i:
                lst.append(string[i + 1:j])
                i = j + 1
            else:
                lst.append(string[i:])
                break
        i += 1

    return l

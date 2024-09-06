from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    output = []
    while paren_string:
        idx = paren_string.find('(')
        if idx == -1:
            output.append(paren_string)
            break
        output.append(paren_string[:idx + 1])
        paren_string = paren_string[idx + 1:]
    return output


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
    index = 0
    for char in paren_string:
        if char == '(':
            if index == 0 or paren_string[index - 1] != ')':
                result.append('')
        index += 1
        while char == '(':
            result.append(paren_string[index])
            index += 1
            if index == len(paren_string):
                break
        else:
            result.append('')
    return result
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

    i = 0
    j = 0
    temp = ''

    while i < len(paren_string):

        if paren_string[i] == "(":
            j = i + 1
            temp = '('

        elif paren_string[i] == ")":
            temp += ')'

            if j == i:
                result.append(temp)
                temp = ''

            elif j < i:
                result.append(temp)
                temp = ''
                j = 0

        i += 1

    return result


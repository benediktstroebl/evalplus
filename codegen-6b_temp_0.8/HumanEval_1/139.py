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

    open_braces = 0
    i = 0

    while i < len(paren_string):
        char = paren_string[i]
        if char == '(':
            open_braces += 1

        elif char == ')':
            open_braces -= 1

        elif char == ' ':
            i += 1  # skip over spaces

        else:
            if open_braces == 0:
                result.append(paren_string[i : i + 1])
                i += 1
            else:
                result.append(char)

            while open_braces != 0:
                i += 1
                result.append(paren_string[i])

    return result


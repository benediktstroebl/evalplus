from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    for i in range(len(paren_string)):
        paren_string = paren_string.replace(' ', '')
        if paren_string[i] == '(':
            begin_index = i
            open_braces = 1
            open_braces_end = (i + 1)
            while open_braces != 0:
                if paren_string[open_braces_end] == '(':
                    open_braces += 1
                elif paren_string[open_braces_end] == ')':
                    open_braces -= 1
                open_braces_end += 1
            paren_string = paren_string[:begin_index] + paren_string[open_braces_end:]
    paren_strings = []
    while len(paren_string) != 0:
        char = paren_string[0]
        if char == '(':
            begin_index = 0
            open_braces = 1
            open_braces_end = 1
            while open_braces != 0:
                if paren_string[open_braces_end] == '(':
                    open_braces += 1
                elif paren_string[open_braces_end] == ')':
                    open_braces -= 1
                open_braces_end += 1
            paren_string = paren_string[open_braces_end:]
        elif char == ')':
            begin_index = 0
            open_braces = -1
            open_braces_end = 1
            while open_braces != 0:
                if paren_string[open_braces_end] == '(':
                    open_braces -= 1
                elif paren_string[open_braces_end] == ')':
                    open_braces += 1
                open_braces_end += 1
            paren_string = paren_string[:begin_index] + paren_string[open_braces_end:]
        else:
            paren_strings.append(paren_string[:1])
            paren_string = paren_string[1:]

    return paren_strings


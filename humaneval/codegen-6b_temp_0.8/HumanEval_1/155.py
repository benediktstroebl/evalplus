from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_strings = [paren_string]
    i = 1
    while i < len(paren_strings):
        paren_string = paren_strings[i]
        j = 0
        while j < len(paren_string):
            bracket = paren_string[j]
            if bracket == '(':
                opening_braces = 1
                closing_braces = 0
                k = j + 1
                while opening_braces > closing_braces and k < len(paren_string):
                    if paren_string[k] == '(':
                        opening_braces += 1
                    elif paren_string[k] == ')':
                        closing_braces += 1
                    k += 1
                paren_string = paren_string[:j] + paren_string[j + opening_braces + closing_braces:]
                paren_strings[i] = paren_string
                j -= 1
            j += 1
        i += 1
    return paren_strings[1:]


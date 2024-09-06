from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separated_strings = []
    paren_string = paren_string.replace(" ", "")
    paren_string = paren_string.replace("(", "")
    paren_string = paren_string.replace(")", "")
    while paren_string!= '':
        current_string = ''
        open_paren = paren_string.find("(")
        if open_paren == -1:
            break
        close_paren = paren_string[open_paren:].find(")")
        if close_paren == -1:
            break
        current_string += paren_string[:open_paren]
        current_string += "(" + paren_string[open_paren + 1:close_paren + open_paren] + ")"
        current_string += paren_string[close_paren + open_paren + 1:]
        separated_strings.append(current_string)
        paren_string = current_string
    return separated_strings


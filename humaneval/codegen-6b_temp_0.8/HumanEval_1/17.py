from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # define a string builder
    output_string = ''
    # open and closed parenthesis need to be paired
    open_parens = []
    closed_parens = []
    # ignore spaces
    paren_string = paren_string.strip()
    # if the string is empty, return an empty list
    if not paren_string:
        return []
    # traverse the string, adding chars to output_string
    for char in paren_string:
        if char == '(':
            open_parens.append(char)
        elif char == ')':
            if open_parens:
                closed_parens.append(char)
                open_parens.pop()
            elif open_parens and not closed_parens:
                output_string += char
        elif char == ' ':
            continue
        else:
            output_string += char
    paren_groups = [output_string + closed_paren for closed_paren in closed_parens]
    return paren_groups


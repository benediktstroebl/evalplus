from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parens = 0
    open_paren_loc = []
    output_strings = []
    for i, char in enumerate(paren_string):
        if char == '(':
            open_parens += 1
            open_paren_loc.append(i)
        if char == ')':
            open_parens -= 1
            if open_parens < 0:
                open_parens = 0
                output_strings.append(paren_string[open_paren_loc[0]:open_paren_loc[1]+1])
                open_paren_loc = []
            else:
                open_paren_loc.pop()
    return output_strings


from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parens = []  # List of tuples
    close_parens = []
    current_group = []
    final_groups = []
    for index, char in enumerate(paren_string):
        if char == '(':
            current_group.append(char)
            open_parens.append((index, char))
        elif char == ')':
            current_group.append(char)
            close_parens.append((index, char))

    while open_parens or close_parens:
        if open_parens:
            open_paren, open_paren_index = open_parens.pop(0)
            while open_paren_index < close_parens[0][0]:
                current_group.append(open_paren)
                open_paren_index += 1

        while close_parens and close_parens[0][0] <= open_paren_index:
            close_paren, close_paren_index = close_parens.pop(0)
            current_group.append(close_paren)

        if current_group:

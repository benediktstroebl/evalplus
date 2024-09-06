from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None:
        return []

    stack = []
    separated_strings = []

    for char in paren_string:
        if char =='':
            continue

        if char == '(':
            stack.append('(')
        else:
            stack.pop()
            if len(stack) == 0:
                separated_strings.append(paren_string[0:paren_string.find(char)])
                paren_string = paren_string[paren_string.find(char) + 1:]

    return separated_strings

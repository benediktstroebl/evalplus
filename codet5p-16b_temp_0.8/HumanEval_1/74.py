from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = []
    paren_stack = []
    paren_string = paren_string.replace(' ', '')
    for i, char in enumerate(paren_string):
        if char == '(':
            paren_stack.append(char)
        elif char == ')':
            if paren_stack:
                paren_stack.pop()
            else:
                paren_list.append(paren_string[:i + 1])
                paren_string = paren_string[i + 1:]
                break
    return paren_list


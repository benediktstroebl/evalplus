from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    paren_list = []

    for character in paren_string:
        if character == '(':
            paren_stack.append('(')
        elif character == ')':
            if len(paren_stack) == 0:
                for i in range(2):
                    paren_list.append(')')
                    # print(') is not leftest parenthesis')
                break
            else:
                paren_stack.pop()

    for paren in paren_stack:
        if paren == '(':
            paren_list.append(')')
            # print('( is not leftest parenthesis')

    return paren_list


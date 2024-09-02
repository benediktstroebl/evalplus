from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    splitting_stack: List[str] = []
    paren_stack: List[str] = []

    paren_string = paren_string.strip()

    for index, symbol in enumerate(paren_string):
        if symbol == '(':
            paren_stack.append(index)
        elif symbol == ')':
            if len(paren_stack) > 0:
                result = paren_string[paren_stack.pop() + 1:index]
                splitting_stack.append(result)
            if len(paren_stack) == 0:
                splitting_stack.append(paren_string[:index])
    return splitting_stack


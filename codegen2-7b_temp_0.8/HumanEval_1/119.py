from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            start_index = stack.pop()
            end_index = i
            yield paren_string[start_index + 1:end_index]
            #

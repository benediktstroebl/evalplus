from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    output = []
    if paren_string == '':
        return output

    paren_stack = []
    start_index = 0

    for i, char in enumerate(paren_string):
        if char == '(':
            paren_stack.append(i)
        elif char == ')':
            if len(paren_stack) == 0:
                return []
            output.append(paren_string[start_index:paren_stack[-1] + 1])
            start_index = paren_stack[-1] + 1
            paren_stack.pop()

    return output


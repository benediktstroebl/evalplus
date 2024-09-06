from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = 0
    paren_stack = []
    final_array = []
    s = ""
    for element in paren_string:
        if element == '(':
            stack += 1
            paren_stack.append(element)
        elif element == ')':
            stack -= 1
            paren_stack.pop()
        elif element == ' ':
            pass
        else:
            s += element
    if s == "":
        if stack == 0:
            return [paren_string]
        return s
    else:
        return s.split(')')


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
    # result = []
    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
        elif char == ')':
            x = paren_stack.pop()
            if x == '(':
                # result.append('')
                pass
        else:
            pass
    print(paren_stack)
    # result[0] = ''.join(result[0])
    # return result


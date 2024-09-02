from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO: implement this function
    result = []
    stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            stack.append(paren_string[i])
            i += 1
        elif paren_string[i] == ')':
            if len(stack) == 0:
                result.append('')
                stack.append(paren_string[i])
            else:
                stack.pop()
                if len(stack) == 0:
                    result.append('')
                else:
                    result[-1] += stack.pop()
            i += 1
        else:
            result.append(paren_string[i])
            i += 1
    return result

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []

    start = 0
    end = 0
    while end < len(paren_string):
        if paren_string[end] == '(':
            stack = 1
            end += 1
            while stack != 0:
                if paren_string[end] == '(':
                    stack += 1
                elif paren_string[end] == ')':
                    stack -= 1
                end += 1
        elif paren_string[end] == ')':
            stack = 1
            end += 1
            while stack != 0:
                if paren_string[end] == '(':
                    stack += 1
                elif paren_string[end] == ')':
                    stack -= 1
                end += 1
        else:
            result.append(paren_string[start:end])
            start = end
            end += 1
    result.append(paren_string[start:end])

    return result


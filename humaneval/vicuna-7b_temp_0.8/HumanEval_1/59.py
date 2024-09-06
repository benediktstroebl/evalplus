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
    open_brace_index = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(' and paren_string[i+1] == '(' and paren_string[i+2] != ' ':
            open_brace_index = i+2
        elif paren_string[i] == ')' and paren_string[i+1] == ')':
            if open_brace_index > -1 and open_brace_index < i:
                result.append(paren_string[open_brace_index+1:i])
                open_brace_index = -1
        else:
            open_brace_index = -1
    if open_brace_index > -1 and open_brace_index < len(paren_string):
        result.append(paren_string[open_brace_index+1:])
    return result


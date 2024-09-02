from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    curr_paren = None
    curr_paren_group = None
    result = []
    for char in paren_string:
        if char == '(':
            if curr_paren is not None:
                result.append(curr_paren_group)
            curr_paren_group = ''
            curr_paren = '('
        elif char == ')':
            if curr_paren is not None:
                curr_paren_group += ')'
                curr_paren = None
        elif char == '{':
            if curr_paren is not None:
                result.append(curr_paren_group)
            curr_paren_group = []
            curr_paren = '{'
        elif char == '}':
            if curr_paren is not None:
                curr_paren_group += '}'
                curr_paren = None
        elif char == '[':
            if curr_paren is not None:
                result.append(curr_paren_group)
            curr_paren_group = []
            curr_paren = '['
        elif char == ']':
            if curr_paren is not None:
                curr_paren_group += ']'
                curr_paren = None
        elif char == ' ':
            curr_paren_group += ' '
        else:
            curr_paren_group += char
    if curr_paren is not None:
        result.append(curr_paren_group)
    return result


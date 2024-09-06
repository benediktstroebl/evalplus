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
    curr_brace = ''
    for char in paren_string:
        if char == '(':
            if curr_brace == ')' or curr_brace == '' or curr_brace == 'n':
                result.append(curr_brace)
                curr_brace = '('
            else:
                result.append(curr_brace)
                curr_brace = '('
        elif char == ')' and curr_brace == '(':
            curr_brace = '('
        elif curr_brace == '(' and char == '(':
            result.append(curr_brace)
            curr_brace = '('
        elif char == 'n':
            if curr_brace == '(':
                result.append(curr_brace)
                curr_brace = '('
            else:
                result.append(curr_brace)
                curr_brace = ''
        else:
            if curr_brace == '(':
                result.append(curr_brace)
                curr_brace = '('
            else:
                result.append(curr_brace)
                curr_brace = ''
    return result
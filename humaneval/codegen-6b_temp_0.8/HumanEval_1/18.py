from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    separated = []
    curr_str = ''
    d = {'(': ')', '{': '}', '[': ']'}
    for c in paren_string:
        if c in d:
            curr_str += c
        elif len(curr_str) > 0:
            if d[curr_str[0]] == c:
                curr_str = curr_str[1:]
            else:
                separated.append(curr_str)
                curr_str = ''
        else:
            if c == ' ':
                continue
            separated.append(curr_str)
            curr_str = ''
    if len(curr_str) > 0:
        separated.append(curr_str)
    return separated


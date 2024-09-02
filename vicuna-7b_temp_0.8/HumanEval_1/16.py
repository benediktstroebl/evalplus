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
    open_brace_idx = 0
    for char in paren_string:
        if char == '(':
            if open_brace_idx == 0:
                result.append(paren_string[open_brace_idx:])
                open_brace_idx += 1
            elif open_brace_idx == len(paren_string)-1:
                result.append(paren_string[open_brace_idx:])
                open_brace_idx = 0
            else:
                result.append(paren_string[open_brace_idx:open_brace_idx+2])
                open_brace_idx += 1
        elif char == ')':
            if open_brace_idx == 0:
                result.append(paren_string[open_brace_idx:])
                open_brace_idx += 1
            else:
                result.append(paren_string[open_brace_idx:open_brace_idx+1])
                open_brace_idx += 1
                result.append(paren_string[open_brace_idx:])
                open_brace_idx += 1
    return result

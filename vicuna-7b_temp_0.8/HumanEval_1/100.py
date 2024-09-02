from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_brace_count = 0
    current_group = []
    for char in paren_string:
        if char == '(':
            open_brace_count += 1
        elif char == ')':
            open_brace_count -= 1
        else:
            if open_brace_count == 0:
                current_group.append(char)
        if open_brace_count == 0:
            current_group.append('') # add an empty string to the end to make it a balanced group
    return current_group


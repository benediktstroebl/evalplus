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
    left_brace_index = 0
    result = []
    for char in paren_string:
        if char == '(':
            open_brace_count += 1
        elif char == ')' and open_brace_count > 0:
            open_brace_count -= 1
            if open_brace_count == 0:
                result.append(paren_string[left_brace_index:])
                left_brace_index += 1
        elif char == ' ':
            pass
    if left_brace_index == len(paren_string) - 1:
        result.append(paren_string[left_brace_index:])
    return result

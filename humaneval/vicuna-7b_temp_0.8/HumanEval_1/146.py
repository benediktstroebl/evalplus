from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    group_open_brace_count = 0
    group_close_brace_count = 0
    next_open_brace = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            group_open_brace_count += 1
            next_open_brace = i
        elif paren_string[i] == ')' and group_open_brace_count > 0:
            group_close_brace_count += 1
            if group_close_brace_count % 2 != 0:
                raise ValueError('Input string is not balanced')
            if next_open_brace - i + 1 != 0:
                raise ValueError('Input string is not nested within each other')
            if i - next_open_brace + 1 >= len(paren_string):
                raise ValueError('Input string is not balanced')
            group_open_brace_count -= 1
            group_close_brace_count -= 1
            next_open_brace = i
    return [paren_string[i:j] for i, j in zip([next_open_brace + 1] * (group_open_brace_count - 1) + [next_open_brace],
                                         [next_open_brace] * (group_close_brace_count - 1) + [i])]
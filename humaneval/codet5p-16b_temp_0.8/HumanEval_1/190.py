from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_braces = []
    open_brace_count = 0
    for i in paren_string:
        if i == '(':
            open_braces.append(i)
            open_brace_count += 1
        elif i == ')':
            open_braces.pop()
            open_brace_count -= 1
            if open_brace_count == 0:
                separated_strings.append(''.join(open_braces))
                open_braces = []
    return separated_strings


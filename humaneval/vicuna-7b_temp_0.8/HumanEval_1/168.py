from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def check_balance(s):
        nonlocal open_brace_count
        nonlocal close_brace_count
        open_brace_count = 0
        close_brace_count = 0
        for i, c in enumerate(s):
            if c == '(':
                open_brace_count += 1
            elif c == ')':
                close_brace_count += 1
                if open_brace_count != close_brace_count - 1:
                    return False
            elif c == ' ':
                continue
            else:
                if not check_balance(s[i:]) and not check_balance(s[:i]):
                    return False
        return True

    open_brace_count = 0
    close_brace_count = 0
    return [s for s in paren_string.split() if check_balance(s)]

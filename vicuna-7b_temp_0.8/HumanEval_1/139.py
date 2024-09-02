from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def repl(m: Match) -> str:
        open_brace_index = len(m.group(0))
        close_brace_index = len(m.group(0)) - len(m.group(1))
        return open_brace_index * ')' + (' ' * (close_brace_index - len(m.group(1)) % open_brace_index)) + m.group(2) + ') '

    return re.sub(r'\(.*?\)', repl, paren_string)


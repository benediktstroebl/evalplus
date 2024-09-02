from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def repl(match):
        # Replace all opening and closing parentheses with an empty string
        # and all opening and closing brackets with an empty string
        # This will remove all parentheses and brackets from the input string
        return ''.join(match.group().replace('(', '').replace(')', '').replace('[', '').replace(']', '')
                      .split())
    return [re.sub(r'\(.*?\)', repl, s) for s in (paren_string or '').split()]

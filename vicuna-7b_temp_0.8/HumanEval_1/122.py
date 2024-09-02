from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def extract_pair(opener: str, closer: str) -> str:
        """
        Given a open and close string, extract the content in between them.
        """
        if closer == opener:
            return ''
        else:
            return f'{opener}[{closer}]'

    paren_list = [extract_pair(opener, closer) for openers, closers in separating_pairs(paren_string)]
    return paren_list


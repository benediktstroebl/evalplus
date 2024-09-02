from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # function to check if a group is closed
    def is_closed(s):
        return len(s) == 1 and s == '(' or s == ')'

    def process(s):
        # initialize result list
        result = []
        # iterate over all characters in the input string
        for c in s:
            # if the current character is an opening parenthesis
            if c == '(':
                # if the previous character was a closing parenthesis
                if is_closed(s[
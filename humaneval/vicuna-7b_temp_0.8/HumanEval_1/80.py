from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def is_balanced(s):
        left, right = s, ''
        while left and right:
            if left in '())':
                right = right[1:]
            elif right in '())':
                left = left[1:]
            else:
                return False
        return True

    def repl(match):
        l = match.group().lstrip('(')
        if l:
            return l.rstrip(')')
        return ''
    return repl.sub('', paren_string)

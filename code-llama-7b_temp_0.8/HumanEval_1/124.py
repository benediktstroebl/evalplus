from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def get_token(paren_string: str) -> str:
        """Returns the first balanced token in a string, removing it from the string"""
        level = 0
        for i, c in enumerate(paren_string):
            if c == '(':
                level += 1
            elif c == ')':
                if level == 0:
                    raise ValueError('No balanced token')
                level -= 1
                if level == 0:
                    return paren_string[:i + 1]
        raise ValueError('No balanced token')

    result = []
    while paren_string:
        result.append(get_token(paren_string))
    return result


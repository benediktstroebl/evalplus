from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [(paren_string[i:j + 1]
            for i, j in zip(*[iter(paren_string)] * 2)
            if (i!= j and paren_string[i] == '(' and paren_string[j] == ')'))
           for group in ([paren_string[:i + 1] for i in range(len(paren_string)) if paren_string[i] == '(']]

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT1: Balanced groups of parens/braces are called "parentheses groups". This hint is only here to googlebalance them.
    # HINT2: In the result list, every string will be either one balanced parentheses group or an empty string.
    # HINT3: The "stack" data structure is useful for this problem.
    return ['']


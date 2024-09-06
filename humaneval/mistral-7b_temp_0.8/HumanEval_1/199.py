from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Your code here

    # return ['()', '(())', '(()())']
    # return ['()', '(())', '(())']

    """
    If your solution is an empty string, it might be because of the closing parentheses.
    Consider using the join() function with the grouping parentheses as a separator.
    This may resolve the issue of unbalanced parentheses.
    """
    return ["".join(reversed(paren_string[paren_string.index(s) + 1 : paren_string.rindex(s)])) for s in "(){}[]"]


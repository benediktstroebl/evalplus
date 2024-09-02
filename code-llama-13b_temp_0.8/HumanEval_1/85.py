from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT1: Try to solve this problem using stack. The idea is to process each brace separately
    # and use the stack to keep track of which braces belong to the same group
    # HINT2: Keep in mind that ')' means that we just closed a group.
    # HINT3: Try to solve this problem in one pass: when should we open a new group and when should we close it?
    pass


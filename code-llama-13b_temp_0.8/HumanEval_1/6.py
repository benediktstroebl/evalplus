from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT1: if this was an interview and you were asked to implement this in
    # an interviewer's language of choice, they may ask you to use stacks
    # HINT2: this is solvable with O(1) space
    # HINT3: if you treat the input string as a linked list of characters, you can solve this in place
    # HINT4: if you want to get really fancy, you can solve this recursively
    # HINT5: the trickiest part of this is coming up with a way to recognize when you've reached the
    # beginning of a new group
    pass


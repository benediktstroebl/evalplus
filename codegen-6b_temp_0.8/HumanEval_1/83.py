from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    brackets = []
    # start with an empty string as a group
    brackets.append('')
    for char in paren_string:
        # if we see a left parenthesis, we need to make a new subgroup containing the current group and adding
        # a left bracket to it
        if char == '(':
            brackets.append('')
        # if we see a right parenthesis, we need to get the last list item (which is the current group)
        # and add a right bracket to it
        elif char == ')':
            brackets.pop()
        # we can add any character to a group, so add it to the last group
        else:
            brackets[-1] += char
    return [g for g in brackets if g]


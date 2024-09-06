from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # keep track of how many parenthesis are open
    open_count = 0
    start_index = 0
    groups = []
    # loop through the string
    for i, c in enumerate(paren_string):
        if c == '(':
            # if we start to see an open parenthesis, and we have one open already,
            # this is the start of a new group
            if open_count > 0:
                groups.append(paren_string[start_index:i])
                start_index = i
            # we are starting a new group
            open_count += 1
        elif c == ')':
            # we are closing a parenthesis
            open_count -= 1
            # if we close one, and we are back to zero,
            # this is the end of the group
            if open_count == 0:
                groups.append(paren_string[start_index:i + 1])
                start_index = i + 1
    # check to see if there is a group left over
    if start_index!= len(paren_string):
        groups.append(paren_string[start_index:])
    return groups


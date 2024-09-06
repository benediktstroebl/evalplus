from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    curr_group = []
    groups = []
    in_group = False
    last_brace = 0

    for i, c in enumerate(paren_string):
        if c == '(':
            # open brace
            # if we're in an group, store the current indices
            # otherwise, just append to the starter of the group
            if in_group:
                curr_group.append(i)
            else:
                curr_group.append(i - last_brace)

            in_group = True
            last_brace = i

        if c == ')':
            curr_group.append(i)
            in_group = False
            groups.append(paren_string[last_brace: curr_group[0]])
            last_brace = curr_group[-1]

    groups.append(paren_string[last_brace:])

    return groups


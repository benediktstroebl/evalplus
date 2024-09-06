from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initializing the output array
    output = []
    # initializing the group string
    group = ""

    for char in paren_string:
        # if the current character is an open brace
        if char == '(':
            # if we already have a group, append that to the output array and initialize a new string
            if len(group) > 0:
                output.append(group)
                group = ''
            # append the open brace to the group
            group += '('
        # if the current character is a close brace
        elif char == ')':
            # if we already have a group, append that to the output array and initialize a new string
            if len(group) > 0:
                output.append(group)
                group = ''
            # append the close brace to the group
            group += ')'
        # else, the current character is a space, we don't care about spaces
        else:
            pass

    # append the last group to the output array
    output.append(group)

    return output


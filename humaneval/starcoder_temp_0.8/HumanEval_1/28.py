from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # create a new list
    groups = []

    # create a new empty string
    current_group = ''

    # create a variable to keep track of the number of open parens
    open_count = 0

    for char in paren_string:
        # if there is an open paren, add it to the empty string
        if char == '(':
            open_count += 1
            current_group += char

        # if there is a closed paren, add it to the string
        elif char == ')':
            open_count -= 1
            current_group += char

            # if we're at 0 open parens, that means we've closed a group
            if open_count == 0:
                groups.append(current_group)

                # reset the current group
                current_group = ''

    return groups


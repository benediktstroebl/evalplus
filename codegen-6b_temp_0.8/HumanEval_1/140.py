from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    paren_stack = []
    # Opening paren of the current group
    open_paren_index = 0

    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            paren_stack.append(i)
            open_paren_index += 1
        elif paren_string[i] == ")":
            if open_paren_index == 0:
                return []
            # If the current paren is closed, add the group to the list
            # and add the closing paren to the new group
            close_paren_index = paren_stack.pop()
            group = paren_string[open_paren_index:close_paren_index + 1]
            # loop starts over the group we just added
            open_paren_index += 1
            result.append(group)

    return result


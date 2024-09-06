from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """
    Find the index of the rightmost opening parenthesis first. Then find the index of the rightmost closing
    parenthesis that matches the opening parenthesis that is rightmost in the string.
    Take that substring and check if it is balanced. Keep doing this until there are no more parentheses.
    """
    groups = []
    curr_left_idx = None
    curr_right_idx = None
    curr_string = ''
    for idx, char in enumerate(paren_string):
        if char == '(':
            if curr_left_idx is None:
                curr_left_idx = idx
            curr_string += char
        elif char == ')':
            if curr_left_idx is not None:
                curr_string += char
                if curr_right_idx is None:
                    curr_right_idx = idx
                elif idx > curr_right_idx:
                    curr_right_idx = idx
            elif curr_left_idx is None:
                curr_string += char
            else:
                raise ValueError('String is unbalanced')

    curr_string = curr_string.strip()

    if curr_left_idx is not None and curr_right_idx is not None:
        curr_right_idx = curr_right_idx + 1
        curr_string = curr_string[curr_left_idx:curr_right_idx]
        if check_paren_balance(curr_string) is True:
            groups.append(curr_string)
            curr_string = ''
            curr_left_idx = None
            curr_right_idx = None
    elif curr_left_idx is not None:
        curr_string = paren_string[curr_left_idx:].strip()

    if curr_string != '':
        groups.extend(separate_paren_groups(curr_string))
    return groups


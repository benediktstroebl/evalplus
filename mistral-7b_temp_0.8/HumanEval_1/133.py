from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initializing an empty list
    paren_list = []
    # initializing the current character to first character in the string
    current_char = paren_string[0]
    # initializing counter for how many left brackets need to be closed
    left_counter = 0

    for character in paren_string:
        if character == '(':
            left_counter += 1
        elif character == ')':
            left_counter -= 1
        elif character == ' ':
            pass
        else:
            raise ValueError(f"{character} is not a valid character")

        # if the current character is not a bracket or a space
        if left_counter < 0:
            paren_list.append(current_char)
            current_char = character
            left_counter = 0
        else:
            current_char += character

    # after the loop is complete, the current character is going to be the last character in the string
    # add the last character to the list
    paren_list.append(current_char)

    return p

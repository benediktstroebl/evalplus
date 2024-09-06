from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None or paren_string.isspace():
        return []

    open_paren = 0
    left_paren = 0
    left_paren_count = 0
    right_paren = 0
    right_paren_count = 0
    result = []
    current_string = []
    current_string_append_character = False

    for index in range(len(paren_string)):
        if paren_string[index] == '(':
            open_paren += 1
        elif paren_string[index] == ')':
            right_paren += 1
            right_paren_count += 1
            if right_paren_count == open_paren:
                right_paren_count = 0
                open_paren = 0
        elif paren_string[index] =='':
            if left_paren_count > 0:
                left_paren_count += 1
            elif right_paren_count > 0:
                right_paren_count += 1
            else:
                current_string.append(paren_string[index])
                current_string

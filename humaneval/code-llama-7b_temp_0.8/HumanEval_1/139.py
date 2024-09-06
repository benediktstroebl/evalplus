from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # breakpoint()
    curr_list = []
    prev_char = paren_string[0]
    for idx, char in enumerate(paren_string[1:]):
        if char == prev_char:
            curr_list.append(paren_string[idx : idx + 2])
        prev_char = char
    return curr_list


from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    group_list = []
    open_count = 0
    start_index = 0
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            open_count += 1
        elif paren_string[i] == ")":
            open_count -= 1
        if open_count == 0:
            group_list.append(paren_string[start_index:i+1])
            start_index = i+1
    return group_list

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = list(paren_string)
    current_index = 0
    group_start_index = 0
    result_list = []
    for char_index in range(len(paren_list)):
        if paren_list[char_index] == '(':
            current_index += 1
        if paren_list[char_index] == ')':
            current_index -= 1
        if current_index == 0:
            result_list.append(''.join(paren_list[group_start_index:char_index+1]))
            group_start_index = char_index+1
    return result_list


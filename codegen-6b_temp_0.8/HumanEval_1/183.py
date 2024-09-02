from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Separates the string along the balance of open and closed braces
    if len(paren_string) < 2:
        return [paren_string]
    # Separates the string along the balance of open and closed braces
    index = 0
    output_list = []
    while index < len(paren_string):
        if paren_string[index] == '(':
            open_brace_index = index
            while paren_string[open_brace_index] != ')':
                open_brace_index += 1
            output_list.append(paren_string[index:open_brace_index + 1])
            index = open_brace_index + 1
        else:
            output_list.append(paren_string[index])
            index += 1
    return output_list


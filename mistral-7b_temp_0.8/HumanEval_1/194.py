from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result_string = ""
    group_list = []
    for i, char in enumerate(paren_string):
        if char == "(":
            result_string += char
        elif char == ")":
            group_list.append(result_string)
            result_string = ""
    return group_list


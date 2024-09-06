from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_strings = []
    start_paren = '('
    end_paren = ')'

    # split paren_string into a list of individual strings
    paren_string_list = list(paren_string)

    # run through list of individual strings, starting from the end, until we find the first closing paren
    # create a list of characters between the first and last closing paren
    while end_paren not in paren_string_list:
        paren_string_list.pop()

    start_index = paren_string_list.index(start_paren)
    end_index = paren_string_list.index(end_paren)

    # strip out the start and end parentheses from the string
    paren_string = paren_string_list[start_index + 1: end_index]
    paren_strings.append(paren_string)

    return paren_strings


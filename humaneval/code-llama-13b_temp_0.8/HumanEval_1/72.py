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
    last_index = 0
    for index, character in enumerate(paren_string):
        if character == "(":
            last_index = index
        if character == ")" and paren_string[index - 1] == "(":
            result.append(paren_string[last_index:index + 1])
    return result


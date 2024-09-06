from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    result: List[str] = []
    current_string = ""
    start_index = 0
    for index, character in enumerate(paren_string):
        if character == ")" and current_string:
            if index == start_index:
                result.append(current_string)
                current_string = ""
                start_index = index + 1
            elif paren_string[index - 1] != "(":
                result.append(current_string)
                current_string = ""
                start_index = index + 1
        elif character == "(":
            current_string += character
    return result


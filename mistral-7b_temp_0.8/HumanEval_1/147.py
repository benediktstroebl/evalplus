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
    output_string = []
    current_string = ""

    for i in paren_string:
        if i == "(":
            current_string += i
        elif i == ")":
            if current_string != "":
                current_string += i
                output_string.append(current_string)
                current_string = ""
        else:
            current_string += i

    if current_string != "":
        output_string.append(current_string)

    return output_string


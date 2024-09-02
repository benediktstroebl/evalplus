from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if not paren_string:
        return []

    count = 0
    output = []

    for i in paren_string:
        if i == "(":
            count += 1
            output.append("(")
        elif i == ")":
            count -= 1
            output.append(")")

        if count == 0:
            return output

    return output


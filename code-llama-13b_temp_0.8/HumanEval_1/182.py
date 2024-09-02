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
    current = ""
    index = 0
    while index < len(paren_string):
        if paren_string[index] == "(":
            current += paren_string[index]
            index += 1
            while paren_string[index] != ")":
                current += paren_string[index]
                index += 1
            current += paren_string[index]
            result.append(current)
            current = ""
            index += 1
        else:
            index += 1
    return result


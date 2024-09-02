from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string == "":
        return []
    elif paren_string[0] != "(":
        return [paren_string]
    else:
        # Collect the left part, and remove it from the string
        left_part = ""
        i = 1
        while i < len(paren_string) and paren_string[i] != "(":
            left_part += paren_string[i]
            i += 1
        paren_string = paren_string[i:]
        # Collect the right part, and remove it from the string
        right_part = ""
        i = 0
        while i < len(paren_string) and paren_string[-(i + 1)] != ")":
            right_part += paren_string[-(i + 1)]
            i += 1
        paren_string = paren_string[:-i]
        # Recursively handle the left and right parts
        return [left_part + separate_paren_groups(paren_string)[0] + right_part] + separate_paren_groups(
            paren_string[1:])


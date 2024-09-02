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
    braces = 0
    for char in paren_string:
        if char == "(":
            braces += 1
        elif char == ")":
            if braces > 0:
                braces -= 1
            else:
                result.append(paren_string[0:len(paren_string) - 1])
                paren_string = paren_string[len(paren_string) - 1]
                continue
        if braces == 0:
            result.append(paren_string)
            paren_string = ""
    

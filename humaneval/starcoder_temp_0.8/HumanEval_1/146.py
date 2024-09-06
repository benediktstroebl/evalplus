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
    while paren_string!= "":
        s = paren_string.find("(")
        if s == -1:
            result.append(paren_string)
            break
        else:
            if s > 0:
                result.append(paren_string[:s])
            paren_string = paren_string[s + 1 :]
            e = paren_string.find(")")
            if e == -1:
                break
            else:
                paren_string = paren_string[e + 1 :]
    return result


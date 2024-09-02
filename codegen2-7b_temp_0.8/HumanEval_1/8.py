from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    _paren_string = paren_string.strip()
    paren_string = "(" + _paren_string + ")"
    paren_string = " " + paren_string + " "
    _paren_string = re.sub("\s+", "", paren_string)
    return _paren_string.split("( ) (( )) (( )( )")


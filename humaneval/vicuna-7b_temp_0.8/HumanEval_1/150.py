from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def recur(paren_string):
        if not paren_string:
            return []
        opening_brace = paren_string.find('{')
        closing_brace = paren_string.rfind('}')
        if opening_brace < 0 or closing_brace < 0:
            return []
        if opening_brace == closing_brace + 1:
            return [paren_string[0:opening_brace]]
        middle_strings = [paren_string[opening_brace+1:closing_brace]]
        return [paren_string[0:opening_brace]] + recur(middle_strings) + [paren_string[closing_brace+1:]]
    return recur(paren_string)


from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result: List[str] = []
    open_parentheses: List[int] = []
    current_parens: str = ''
    for index, char in enumerate(paren_string):
        if char == '(':
            open_parentheses.append(index)
            current_parens += char
        elif char == ')':
            current_parens += char
            open_parentheses.pop()
        if not open_parentheses:
            result.append(current_parens)
            current_parens = ''
    return result


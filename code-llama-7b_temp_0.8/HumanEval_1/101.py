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

    result: List[str] = []
    open_brackets = 0
    current_string = []

    for character in paren_string:
        if character == '(':
            open_brackets += 1
        elif character == ')':
            if not open_brackets:
                raise ValueError('Imbalanced parentheses in the input')
            open_brackets -= 1
        current_string.append(character)
        if not open_brackets:
            result.append(''.join(current_string))
            current_string = []

    if open_brackets:
        raise ValueError('Imbalanced parentheses in the input')

    return result


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
    current_open_brace = None
    for c in paren_string:
        if c == '(':
            if current_open_brace is not None:
                result.append(current_open_brace.strip())
                current_open_brace = None
            else:
                current_open_brace = '('
        elif c == ')':
            if current_open_brace is None:
                raise ValueError("Missing open brace")
            current_open_brace = None
        elif c == ' ':
            # ignore spaces
            pass
        else:
            raise ValueError(f"Invalid character: {c}")
    if current_open_brace is not None:
        result.append(current_open_brace.strip())
    return result

